from setuptools import setup, find_packages
from thecut.durationfield import __title__, __url__, __version__

setup(
    name=__title__,
    author='Josh Crompton',
    author_email='josh.crompton@thecut.net.au',
    url=__url__,
    description=(
        'Form and model fields for storing durations on Django models'
        'as ISO 8601 compliant strings, and returning relativedelta objects.'
    ),
    namespace_packages=['thecut'],
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'isodate == 0.4.9',
        'python-dateutil == 2.1'
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
