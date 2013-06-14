# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
import isodate
from mock import Mock
from thecut.durationfield import fields
from unittest import TestCase


class TestISO8061DurationField(TestCase):

    def setUp(self):
        self.field = fields.ISO8601DurationField()

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


class TestRelativeDeltaField(TestCase):

    def setUp(self):
        self.field = fields.RelativeDeltaField()

    def test_returns_a_relativedelta_when_given_an_iso8601_formatted_string(self):

        d = relativedelta()
        self.assertEqual(type(d), type(self.field.to_python('P1M')))

    def test_returns_an_iso8601_formatted_string(self):
        # Given a timedelta, get_prep_value should return a value suitable for
        # saving to the db. Specifically, an ISO8601 formatted duration.
        duration = relativedelta(months=1.0)
        self.assertEqual(self.field.get_prep_value(duration), 'P1.0M')

    def test_converts_given_relativedelta_to_a_duration(self):
        self.field.convert_relativedelta_to_duration = Mock(return_value=isodate.parse_duration('P1M'))
        delta = relativedelta(months=1)
        self.field.get_prep_value(delta)

        self.assertTrue(self.field.convert_relativedelta_to_duration.called)
        self.assertTrue(self.field.convert_relativedelta_to_duration.called_with(delta))

    def test_can_convert_relativedelta_months(self):
        delta = relativedelta(months=1)
        duration = isodate.duration.Duration(months=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_days(self):
        delta = relativedelta(days=1)
        duration = isodate.duration.Duration(days=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_seconds(self):
        delta = relativedelta(seconds=1)
        duration = isodate.duration.Duration(seconds=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_microseconds(self):
        delta = relativedelta(microseconds=1)
        duration = isodate.duration.Duration(microseconds=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_minutes(self):
        delta = relativedelta(minutes=1)
        duration = isodate.duration.Duration(minutes=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_hours(self):
        delta = relativedelta(hours=1)
        duration = isodate.duration.Duration(hours=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_months(self):
        delta = relativedelta(months=1)
        duration = isodate.duration.Duration(months=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_years(self):
        delta = relativedelta(years=1)
        duration = isodate.duration.Duration(years=1)
        self.assertEqual(self.field.convert_relativedelta_to_duration(delta),
                         duration)

    def test_converts_given_complex_relativedelta_to_a_duration(self):
        delta = relativedelta(months=1, days=2)
        duration_string = self.field.get_prep_value(delta)
        self.assertEqual(duration_string, 'P1M2D')

    def test_converts_given_duration_to_relativedelta(self):
        self.field.convert_duration_to_relativedelta = Mock(return_value=relativedelta())
        self.field.to_python('P1M')
        self.assertTrue(self.field.convert_duration_to_relativedelta.called)

    def test_can_convert_duration_years(self):
        duration = isodate.duration.Duration(years=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.years, 1)

    def test_can_convert_duration_months(self):
        duration = isodate.duration.Duration(months=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.months, 1)

    def test_can_convert_duration_weeks(self):
        duration = isodate.duration.Duration(weeks=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.days, 7)

    def test_can_convert_duration_days(self):
        duration = isodate.duration.Duration(days=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.days, 1)

    def test_can_convert_duration_hours(self):
        duration = isodate.duration.Duration(hours=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.hours, 1)

    def test_can_convert_duration_minutes(self):
        duration = isodate.duration.Duration(minutes=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.minutes, 1)

    def test_can_convert_duration_seconds(self):
        duration = isodate.duration.Duration(seconds=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.seconds, 1)

    def test_can_convert_duration_microseconds(self):
        duration = isodate.duration.Duration(microseconds=1)
        delta = self.field.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.microseconds, 1)

    def test_to_python_returns_relativedelta_if_given_a_relativedelta(self):
        delta = relativedelta(days=1)
        self.assertEqual(type(delta), type(self.field.to_python(delta)))
