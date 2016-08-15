===============================
Welcome to thecut-durationfield
===============================


.. image:: https://travis-ci.org/thecut/thecut-durationfield.svg
    :target: https://travis-ci.org/thecut/thecut-durationfield

.. image:: https://codecov.io/github/thecut/thecut-durationfield/coverage.svg
    :target: https://codecov.io/github/thecut/thecut-durationfield

.. image:: https://readthedocs.org/projects/thecut-durationfield/badge/?version=latest
    :target: http://thecut-durationfield.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This app provides a custom Django model field, ``RelativeDeltaField``, and
related form fields and widgets. ``RelativeDeltaField`` stores time durations
using `ISO 8601`_ representations, and returns ``dateutil.relativedelta``
objects which may be used directly with ``datetime.datetime`` objects.

This project was inspired by packages such as `django-durationfield`_. However,
this project focuses on:

#. providing a database-agnostic, standards-compliant way of storing the
   durations in the database (using `ISO 8601`_).
#. returning ``dateutil.relativedelta`` objects that can be used to perform
   calculations on ``datetime.datetime`` objects.

Note that `django-durationfield`_ provides the ability to filter querysets
based on the relative size of the stored duration, which is not possible with
this project. I.e., you can't use ``__lt`` and ``__gt`` etc., when filtering
by fields provided by this project.


Documentation
-------------

The full documentation is at https://thecut-durationfield.readthedocs.org.


Quickstart
----------

Install ``thecut-durationfield`` using the :ref:`installation`.


Credits
-------

See :ref:`credits`.


.. _`ISO 8601`: http://en.wikipedia.org/wiki/ISO_8601#Durations
.. _`django-durationfield`: https://github.com/johnpaulett/django-durationfield
.. _`pypi`: http://pypi.python.org/pypi/django-timezone-field/
.. _`pip`: http://www.pip-installer.org/
