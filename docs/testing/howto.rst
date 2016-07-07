==================
Running unit tests
==================


Using your system's Python / Django
-----------------------------------

You can perform basic testing against your system's Python / Django.

1. Install the test suite requirements::

    $ pip install -r requirements-test.txt

2. Ensure a version of Django is installed::

    $ pip install Django

3. Run the test runner::

    $ python runtests.py


Using a virtualenv
------------------

You can use ``virtualenv`` to test without polluting your system's Python environment.

1. Install ``virtualenv``::

    $ pip install virtualenv

2. Create and activate a ``virtualenv``::

    $ cd thecut-exampleapp
    $ virtualenv .
    $ source bin/activate
    (thecut-exampleapp) $

3. Follow 'Using your system's Python / Django' above.


Using tox
---------------------------------

You can use tox to automatically test the application on a number of different
Python and Django versions.

1. Install ``tox``::

    $ pip install -r requirements-test.txt

2. Run ``tox``::

    (thecut-exampleapp) $ tox --recreate

Tox assumes that a number of different Python versions are available on your
system. If you do not have all required versions of Python installed on your
system, running the tests will fail. See ``tox.ini`` for a list of Python
versions that are used during testing.

Test coverage
-------------

The included ``tox`` configuration automatically detects test code coverage with ``coverage``::

      $ coverage report
