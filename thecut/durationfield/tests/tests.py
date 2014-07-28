# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.core.exceptions import ValidationError
import isodate
from mock import Mock
from .. import models
from .. import utils
from unittest import TestCase


class TestISO8061DurationField(TestCase):

    def setUp(self):
        self.field = models.ISO8601DurationField()

    def test_to_python_returns_a_duration_when_given_a_duration(self):

        duration = isodate.parse_duration('P1M')
        self.assertEqual(type(duration), type(self.field.to_python(duration)))

    def test_to_python_returns_none_when_given_none(self):

        self.assertEqual(None, self.field.to_python(None))

    def test_to_python_returns_none_when_given_an_empty_string(self):

        self.assertEqual(None, self.field.to_python(''))

    def test_to_python_returns_a_duration_when_given_a_validly_formatted_string(self):

        self.assertEqual(isodate.duration.Duration,
                         type(self.field.to_python('P1M')))

    def test_to_python_raises_an_error_when_given_an_invalid_string(self):

        self.assertRaises(ValidationError, self.field.to_python, 'abc')

    def test_get_prep_value_raises_an_error_when_called_with_an_invalid_object(self):

        self.assertRaises(ValidationError, self.field.get_prep_value, 'abc')

    def test_get_prep_value_returns_none_when_given_none(self):

        self.assertEqual(None, self.field.get_prep_value(None))

    def test_get_prep_value_is_isomorphic(self):

        duration = isodate.parse_duration('P1M')
        self.assertEqual('P1M', self.field.get_prep_value(duration))

        duration = isodate.parse_duration('P1.0M')
        self.assertEqual('P1.0M', self.field.get_prep_value(duration))


class TestRelativeDeltaField(TestCase):

    def setUp(self):
        self.field = models.RelativeDeltaField()

    def test_returns_a_relativedelta_when_given_an_iso8601_formatted_string(self):

        d = relativedelta()
        self.assertEqual(type(d), type(self.field.to_python('P1M')))

    def test_returns_none_if_given_an_empty_string(self):
        self.assertEqual(None, self.field.to_python(''))

    def test_returns_an_iso8601_formatted_string(self):
        # Given a timedelta, get_prep_value should return a value suitable for
        # saving to the db. Specifically, an ISO8601 formatted duration.
        duration = relativedelta(months=1.0)
        self.assertEqual(self.field.get_prep_value(duration), 'P1M')

    def test_converts_none_to_none(self):
        self.assertEqual(self.field.get_prep_value(None), None)

    def test_converts_given_relativedelta_to_a_duration(self):
        utils.convert_relativedelta_to_duration = Mock(return_value=isodate.parse_duration('P1M'))
        delta = relativedelta(months=1)
        self.field.get_prep_value(delta)

        self.assertTrue(utils.convert_relativedelta_to_duration.called)
        self.assertTrue(utils.convert_relativedelta_to_duration.called_with(delta))

    def test_can_convert_relativedelta_months(self):
        delta = relativedelta(months=1)
        duration = isodate.duration.Duration(months=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_days(self):
        delta = relativedelta(days=1)
        duration = isodate.duration.Duration(days=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_seconds(self):
        delta = relativedelta(seconds=1)
        duration = isodate.duration.Duration(seconds=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_microseconds(self):
        delta = relativedelta(microseconds=1)
        duration = isodate.duration.Duration(microseconds=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_minutes(self):
        delta = relativedelta(minutes=1)
        duration = isodate.duration.Duration(minutes=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_hours(self):
        delta = relativedelta(hours=1)
        duration = isodate.duration.Duration(hours=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_can_convert_relativedelta_years(self):
        delta = relativedelta(years=1)
        duration = isodate.duration.Duration(years=1)
        self.assertEqual(utils.convert_relativedelta_to_duration(delta),
                         duration)

    def test_converts_given_complex_relativedelta_to_a_duration(self):
        delta = relativedelta(months=1, days=2)
        duration_string = self.field.get_prep_value(delta)
        self.assertEqual(duration_string, 'P1M2D')

    def test_converts_given_duration_to_relativedelta(self):
        utils.convert_duration_to_relativedelta = Mock(return_value=relativedelta())
        self.field.to_python('P1M')
        self.assertTrue(utils.convert_duration_to_relativedelta.called)

    def test_can_convert_duration_years(self):
        duration = isodate.duration.Duration(years=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.years, 1)

    def test_can_convert_duration_months(self):
        duration = isodate.duration.Duration(months=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.months, 1)

    def test_can_convert_duration_weeks(self):
        duration = isodate.duration.Duration(weeks=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.days, 7)

    def test_can_convert_duration_days(self):
        duration = isodate.duration.Duration(days=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.days, 1)

    def test_can_convert_duration_hours(self):
        duration = isodate.duration.Duration(hours=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.seconds, 60*60)

    def test_can_convert_duration_minutes(self):
        duration = isodate.duration.Duration(minutes=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.seconds, 60)

    def test_can_convert_duration_seconds(self):
        duration = isodate.duration.Duration(seconds=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.seconds, 1)

    def test_can_convert_duration_microseconds(self):
        duration = isodate.duration.Duration(microseconds=1)
        delta = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(delta.microseconds, 1)

    def test_to_python_returns_relativedelta_if_given_a_relativedelta(self):
        delta = relativedelta(days=1)
        self.assertEqual(type(delta), type(self.field.to_python(delta)))

    def test_can_add_a_relative_delta_for_a_partial_month_to_a_datetime(self):
        # A relativdelta with a non-integer value for month/year/week/days
        # cannot be added to a datetime (see
        # https://bugs.launchpad.net/dateutil/+bug/1204017). So we need to
        # manually cast these to be integers. We won't be getting back exactly
        # what we expect, but it's probably better than propograting a type
        # error from deep inside relativedelta.

        duration = isodate.duration.Duration(months=1.5)
        one_and_a_half_months = utils.convert_duration_to_relativedelta(duration)
        january_first = datetime(2013, 1, 1)
        february_first = datetime(2013, 2, 1)
        self.assertEqual(january_first + one_and_a_half_months, february_first)

    def test_can_add_a_relative_delta_for_a_partial_year_to_a_datetime(self):
        # A relativdelta with a non-integer value for month/year/week/days
        # cannot be added to a datetime (see
        # https://bugs.launchpad.net/dateutil/+bug/1204017). So we need to
        # manually cast these to be integers. We won't be getting back exactly
        # what we expect, but it's probably better than propograting a type
        # error from deep inside relativedelta.

        duration = isodate.duration.Duration(years=1.5)
        one_and_a_half_years = utils.convert_duration_to_relativedelta(duration)
        january_first = datetime(2013, 1, 1)
        self.assertEqual(january_first + one_and_a_half_years, datetime(2014, 1, 1))

    def test_can_add_a_relative_delta_for_a_partial_day_to_a_datetime(self):
        # Actually, turns out 1.5 days is ok, since it gets magically converted
        # to one day and 12 hours.
        duration = isodate.duration.Duration(days=1.5)
        one_and_a_half_days = utils.convert_duration_to_relativedelta(duration)
        self.assertEqual(one_and_a_half_days.days, 1)

        january_first = datetime(2013, 1, 1)
        self.assertEqual(january_first + one_and_a_half_days,
                         datetime(2013, 1, 2, 12, 0, 0))
