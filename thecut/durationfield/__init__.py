# -*- coding: utf-8 -*-
"""Create new django model field (extended CharField) to accept ISO 8601
defined representation.

http://en.wikipedia.org/wiki/ISO_8601#Durations

P is the duration designator (historically called "period") placed at the start
of the duration representation.
---
Y is the year designator that follows the value for the number of years.
M is the month designator that follows the value for the number of months.
W is the week designator that follows the value for the number of weeks.
D is the day designator that follows the value for the number of days.
---
T is the time designator that precedes the time components of the
  representation.
H is the hour designator that follows the value for the number of hours.
M is the minute designator that follows the value for the number of minutes.
S is the second designator that follows the value for the number of seconds.

Note: M-month and M-minute can cause ambiguity -- T designator is necessary for
time values.

Example:
P1Y2M10DT2H30M
1 years, 2 months, 10 days, 2:30:00

Thses are then parsed[1] and converted to a python usable delta[2].

Note isodate.parse_duration return either
<type 'datetime.timedelta'> or <class 'isodate.duration.Duration'>
depending on whether it's possible to convert the

[1] isodate https://pypi.python.org/pypi/isodate
[2] dateutil.relativedelta for consistency.
"""
