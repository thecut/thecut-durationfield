# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import Field
from . import widgets


class RelativeDeltaField(Field):

    widget = widgets.RelativeDeltaSelect
