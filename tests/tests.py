# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ValidationError
import isodate
from thecut.durationfield.fields import ISO8601DurationField
from unittest import TestCase


class TestISO8061DurationField(TestCase):

    def setUp(self):
        self.field = ISO8601DurationField()

    def test_to_python_returns_a_duration_when_given_a_duration(self):

        duration = isodate.parse_duration('P1M')
        self.assertEqual(type(duration), type(self.field.to_python(duration)))

    def test_to_python_returns_a_duration_when_given_none(self):

        self.assertEqual(isodate.duration.Duration,
                         type(self.field.to_python(None)))

    def test_to_python_returns_a_duration_when_given_an_empty_string(self):

        self.assertEqual(isodate.duration.Duration,
                         type(self.field.to_python('')))

    def test_to_python_returns_a_duration_when_given_a_validly_formatted_string(self):

        self.assertEqual(isodate.duration.Duration,
                         type(self.field.to_python('P1M')))

    def test_to_python_raises_an_error_when_given_an_invalid_string(self):

        self.assertRaises(ValidationError, self.field.to_python, 'abc')

    def test_get_prep_value_raises_an_error_when_called_with_an_invalid_object(self):

        self.assertRaises(ValidationError, self.field.get_prep_value, 'abc')

    def test_get_prep_value_is_isomorphic(self):

        duration = isodate.parse_duration('P1M')
        self.assertEqual('P1.0M', self.field.get_prep_value(duration))
