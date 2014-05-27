# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import widgets
from django.forms import Field, ChoiceField


class RelativeDeltaChoiceField(ChoiceField):

    widget = widgets.RelativeDeltaSelect


class RelativeDeltaTextInput(Field):

    widget = widgets.RelativeDeltaTextInput
