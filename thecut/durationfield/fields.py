# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from django.db.models import Field, SubfieldBase
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from isodate.isoerror import ISO8601Error
import isodate
from isodate import duration_isoformat

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
        if isinstance(value, isodate.duration.Duration):
            return value

        if value is None or value == '':
            return isodate.duration.Duration()
        try:
            duration = isodate.parse_duration(value)
        except ISO8601Error:
            raise ValidationError(self.default_error_messages['invalid'])
        return duration

    def get_prep_value(self, value):
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

    def to_python(self, value):
        duration = super(RelativeDeltaField, self).to_python(value)
        delta = self.convert_duration_to_relativedelta(duration)
        return delta

    def get_prep_value(self, value):
        # Build the Duration object from the given relativedelta.
        duration = self.convert_relativedelta_to_duration(value)
        duration_string = super(RelativeDeltaField, self).get_prep_value(duration)
        return duration_string

    def convert_relativedelta_to_duration(self, delta):
        """Convert a :py:class:`~datetime.relativedelta.relativedelta` to a
        :py:class:`~isodate.duration.Duration`."""
        duration = isodate.duration.Duration(days=delta.days,
            seconds=delta.seconds, microseconds=delta.microseconds,
            minutes=delta.minutes, hours=delta.hours, months=delta.months,
            years=delta.years)
        return duration

    def convert_duration_to_relativedelta(self, duration):
        """Convert a :py:class:`~isodate.duration.Duration` to a
        :py:class:`~datetime.relativedelta.relativedelta`."""
        delta = relativedelta(years=duration.years, months=duration.months,
            days=duration.days, seconds=duration.tdelta.seconds,
            microseconds=duration.tdelta.microseconds)
        return delta

if add_introspection_rules:
    add_introspection_rules([], ["^thecut\.durationfield\.fields"])
