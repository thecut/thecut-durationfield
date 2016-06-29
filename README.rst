=================
thecut.exampleapp
=================

A reusable application.


Adding this application to your project
---------------------------------------

1. Add ``thecut-exampleapp`` to your project's requirements file::

    $ echo 'thecut-exampleapp' >> requirements.txt

2. Add ``thecut.exampleapp`` to your project's ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        # ...
        'thecut.exampleapp'
    ]

3. Run any app migrations::

    $ python manage.py migrate example


Testing this application manually
---------------------------------

1. Install ``virtualenv``::

    $ pip install virtualenv

2. Create and activate a ``virtualenv``::

    $ cd thecut-exampleapp
    $ virtualenv .
    $ source bin/activate
    (thecut-exampleapp) $

3. Install the test suite requirements::

    (thecut-exampleapp) $ pip install -r requirements-test.txt

4. Run the test runner::

    (thecut-exampleapp) $ python runtests.py


Testing this application with tox
---------------------------------

We can use tox to test thecut.exampleapp on a number of different Python and Django
versions.

Tox assumes that a number of different Python versions are available on your
system. If you do not have all required versions of Python installed on your
system, running the tests will fail. See ``tox.ini`` for a list of Python
versions that are used during testing.

1. Install ``virtualenv``::

    $ pip install virtualenv

2. Create and activate a ``virtualenv``::

    $ cd thecut-exampleapp
    $ virtualenv .
    $ source bin/activate
    (thecut-exampleapp) $

3. Install ``tox``::

    (thecut-exampleapp) $ pip install -r requirements-test.txt

4. Run ``tox``::

    (thecut-exampleapp) $ tox --recreate


Test coverage
-------------

The included ``tox`` configuration automatically detects test code coverage with ``coverage``::

      (thecut-exampleapp) $ coverage report
