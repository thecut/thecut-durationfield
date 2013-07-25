# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms.widgets import TextInput
from django.forms import Field
from isodate import duration_isoformat
from dateutil.relativedelta import relativedelta
from . import utils


class RelativeDeltaWidget(TextInput):

    def _format_value(self, value):

        if isinstance(value, relativedelta):
            duration = utils.convert_relativedelta_to_duration(value)
            value = duration_isoformat(duration)

        return value

    def render(self, name, value, attrs=None):
        value = self._format_value(value)
        return super(RelativeDeltaWidget, self).render(name, value, attrs)

    def _has_changed(self, initial, data):
        return super(RelativeDeltaWidget, self)._has_changed(
            self._format_value(initial), data)


class RelativeDeltaFormField(Field):

    widget = RelativeDeltaWidget
