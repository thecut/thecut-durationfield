=================
thecut.example
=================

A reusable application.


Adding this application to your project
---------------------------------------

1. Add ``thecut-example`` to your project's requirements file::

    $ echo 'thecut-example' >> requirements.txt

2. Add ``thecut.example`` to your project's ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        # ...
        'thecut.example'
    ]

3. Run any app migrations::

    $ python manage.py migrate example


Testing this application manually
---------------------------------

1. Install ``virtualenv``::

    $ pip install virtualenv

2. Create and activate a ``virtualenv``::

    $ cd thecut-example
    $ virtualenv .
    $ source bin/activate
    (thecut-example) $

3. Install the test suite requirements::

    (thecut-example) $ pip install -r requirements-test.txt

4. Run the test runner::

    (thecut-example) $ python runtests.py


Testing this application with tox
---------------------------------

We can use tox to test thecut.example on a number of different Python and Django
versions.

Tox assumes that a number of different Python versions are available on your
system. If you do not have all required versions of Python installed on your
system, running the tests will fail. See ``tox.ini`` for a list of Python
versions that are used during testing.

1. Install ``virtualenv``::

    $ pip install virtualenv

2. Create and activate a ``virtualenv``::

    $ cd thecut-example
    $ virtualenv .
    $ source bin/activate
    (thecut-example) $

3. Install ``tox``::

    (thecut-example) $ pip install -r requirements-test.txt

4. Run ``tox``::

    (thecut-example) $ tox --recreate


Test coverage
-------------

The included ``tox`` configuration automatically detects test code coverage with ``coverage``::

      (thecut-example) $ coverage report
