# -*- coding: utf-8 -*-
""" Utility functions to convert back and forth between a ISO 8601
representation as string and time delta object.
"""
import datetime
import isodate
from isodate.isoerror import ISO8601Error
from dateutil import relativedelta

def isodate_to_relativedelta(value):
    """
    Accepts `string` or :py:class:`isodate.duration.Duration`
    Returns :py:class:`dateutil.relativedelta.relativedelta`

    :py:class:`isodate.duration.Duration` is a super-set of
    `datetime.timedelta`.

    attributes:
    {'tdelta': datetime.timedelta(),
     'months': 0.0,
     'years': 0.0'}

    `datetime.timedelta()` attributes:
    {'days',
     'seconds',
     'microseconds'}

    `datetime.timedelta` is returned by the function `isodate.parse_duration()`
    should duration string be sufficiently simple.

    In the more complicated case (ie duration is greater than days) an
    `isodate.duration.Duration` object is returned.

    """

    if isinstance(value, basestring):
        try:
            isodate_to_convert = isodate.parse_duration(value)
        except ISO8601Error:
            """
            ISO8601 duration representation must be passed in to function, if not
            go shall not be passed.
            """
            raise
    else:
        """ Should `value` not be a string type is duck.
        """
        isodate_to_convert = value

    new_rdelta = relativedelta.relativedelta()

    try:
        """ Should :py:class:isodate.duration.Duration be greater than
        seconds/minutes it has addition months/years as well as
        """
        datetime_to_convert = isodate_to_convert.tdelta
        new_rdelta.months = isodate_to_convert.months
        new_rdelta.years = isodate_to_convert.years
    except AttributeError:
        """ Should :py:class:`isodate.duration.Duration` not have tdelta
        attribute :py:type:`datetime.timedelta` is returned.
        """
        datetime_to_convert = isodate_to_convert

    new_rdelta.days = datetime_to_convert.days
    new_rdelta.seconds = datetime_to_convert.seconds
    new_rdelta.microseconds = datetime_to_convert.microseconds

    return new_rdelta
