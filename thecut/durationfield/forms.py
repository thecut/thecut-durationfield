# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import Field, ChoiceField
from . import widgets


class RelativeDeltaChoiceField(ChoiceField):

    widget = widgets.RelativeDeltaSelect


class RelativeDeltaTextInput(Field):

    widget = widgets.RelativeDeltaTextInput
