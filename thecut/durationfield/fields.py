# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models.fields import TextField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.forms.util import ValidationError
from django.forms import TextInput
from isodate.isoerror import ISO8601Error
from thecut.durationfield.utils import isodate_to_relativedelta

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    add_introspection_rules = None


@python_2_unicode_compatible
class DurationField(TextField):
    """Field (extended TextField) to accept ISO 8601 defined representation.
    """

    description = _("Duration of time in ISO 8601 representation")
    default_error_messages = {
        'invalid': _("This value must be in ISO 8601 Duration format."),
        'unknown_type': _("The value's type could not be converted"),
    }

    def formfield(self, *args, **kwargs):
        kwargs.update({'widget': TextInput})
        return super(TextField, self).formfield(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def to_python(self, value):
        """
        :py:class:`dateutil.relativedelta.relativedelta` is returned
        from ISO8601 duration formatted string or
        :py:class:`isodate.duration.Duration`.
        """
        try:
            isodate = isodate_to_relativedelta(value)
        except ISO8601Error:
            raise ValidationError(self.error_messages['invalid'])
        return isodate

if add_introspection_rules:
    add_introspection_rules([], ["^thecut\.durationfield\.fields"])

