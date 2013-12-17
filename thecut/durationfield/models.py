# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from isodate.isoerror import ISO8601Error
import isodate
from dateutil.relativedelta import relativedelta
from . import utils
from . import forms


try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    add_introspection_rules = None


class ISO8601DurationField(models.Field):
    """Store and retrieve ISO 8601 formatted durations.

    """

    description = _("A duration of time (ISO 8601 format)")

    __metaclass__ = models.SubfieldBase

    default_error_messages = {
        'invalid': _("This value must be in ISO 8601 Duration format."),
        'unknown_type': _("The value's type could not be converted"),
    }

    def __init__(self, *args, **kwargs):
        self.max_length = kwargs['max_length'] = 64
        super(ISO8601DurationField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        """
        :returns: A duration object parsed from the given value.
        :rtype: :py:class:`~isodate.duration.Duration`

        """
        # DB value is null
        if value is None:
            return None

        # DB value is empty
        if value == '':
            return isodate.duration.Duration()

        if isinstance(value, isodate.duration.Duration):
            return value

        try:
            duration = isodate.parse_duration(value)
        except ISO8601Error:
            raise ValidationError(self.default_error_messages['invalid'])
        return duration

    def get_prep_value(self, value):

        # Value in DB should be null.
        if value is None:
            return None

        if not isinstance(value, isodate.duration.Duration):
            raise ValidationError('Cannot convert objects that are not Durations.')

        return isodate.duration_isoformat(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)


class RelativeDeltaField(ISO8601DurationField):
    """Store and retrieve :py:class:`~datetime.relativedelta.relativedelta`.

    Stores the relativedelta as a string representation of a
    :py:class:`~isodate.duration.Duration`.
    """

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.RelativeDeltaChoiceField}
        defaults.update(kwargs)
        return super(RelativeDeltaField, self).formfield(**defaults)

    def to_python(self, value):

        # DB value is null
        if value is None:
            return None

        if isinstance(value, relativedelta):
            return value

        duration = super(RelativeDeltaField, self).to_python(value)

        delta = utils.convert_duration_to_relativedelta(duration)

        return delta

    def get_prep_value(self, value):

        # Value in DB should be null
        if value is None:
            return None

        # Build the Duration object from the given relativedelta.
        duration = utils.convert_relativedelta_to_duration(value)
        duration_string = super(RelativeDeltaField, self).get_prep_value(duration)

        return duration_string

    def value_to_string(self, obj):
        val = self._get_val_from_obj(obj)
        s = self.get_prep_value(val)
        return '' if s is None else s

if add_introspection_rules:
    add_introspection_rules([], ['^thecut\.durationfield\.models\.ISO8601DurationField',
                                 '^thecut\.durationfield\.models\.RelativeDeltaField'])
