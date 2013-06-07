# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible, smart_text

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    add_introspection_rules = None


@python_2_unicode_compatible
class DurationField(CharField):
    """Field (extended CharField) to accept ISO 8601 defined representation.
    """

    description = _("Duration of time in ISO 8601 representation")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 64
        super(DurationField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"


if add_introspection_rules:
    add_introspection_rules([], ["^thecut\.durationfield\.fields\.duration"])

