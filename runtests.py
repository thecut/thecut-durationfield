import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="thecut.durationfield.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "thecut.durationfield",
        ],
        SITE_ID=1,
        NOSE_ARGS=['-s'],
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['thecut.durationfield.tests.tests']

    # Nose and/or django-nose seems to have some problems with Django 1.7, so
    # we'll use Django's own test runner if it's available. If not, we'll use
    # Nose instead, which is easier than trying to get Django's old test runner
    # to work for us.
    try:
        from django.test.runner import DiscoverRunner
        test_runner = DiscoverRunner()

    except ImportError:
        from django_nose import NoseTestSuiteRunner
        test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
