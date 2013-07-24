# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from django.db.models import Field, SubfieldBase
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
from django import forms
from isodate.isoerror import ISO8601Error
import isodate
from isodate import duration_isoformat

from . import utils

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    add_introspection_rules = None


@python_2_unicode_compatible
class ISO8601DurationField(Field):
    """Store and retrieve ISO 8601 formatted durations.

    """

    description = _("A duration of time (ISO 8601 format)")

    __metaclass__ = SubfieldBase

    default_error_messages = {
        'invalid': _("This value must be in ISO 8601 Duration format."),
        'unknown_type': _("The value's type could not be converted"),
    }

    def __init__(self, *args, **kwargs):
        self.max_length = kwargs['max_length'] = 64
        super(ISO8601DurationField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char({0})'.format(self.max_length)

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


class RelativeDeltaWidget(TextInput):

    def _format_value(self, value):

        if isinstance(value, relativedelta):
            duration = utils.convert_relativedelta_to_duration(value)
            value = isodate.duration_isoformat(duration)

        return value

    def render(self, name, value, attrs=None):
        value = self._format_value(value)
        return super(RelativeDeltaWidget, self).render(name, value, attrs)

    def _has_changed(self, initial, data):
        return super(RelativeDeltaWidget, self)._has_changed(
            self._format_value(initial), data)




class RelativeDeltaFormField(forms.Field):

    widget = RelativeDeltaWidget


class RelativeDeltaField(ISO8601DurationField):
    """Store and retrieve :py:class:`~datetime.relativedelta.relativedelta`.

    Stores the relativedelta as a string representation of a
    :py:class:`~isodate.duration.Duration`.
    """

    def formfield(self, **kwargs):
        defaults = {'form_class': RelativeDeltaFormField}
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
    add_introspection_rules([], ["^thecut\.durationfield\.fields"])
