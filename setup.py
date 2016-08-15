from __future__ import print_function
import codecs
import io
import os
from thecut.durationfield import __version__
from setuptools import setup, find_packages
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        filename = os.path.join(here, filename)
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'HISTORY.rst')

setup(
    # General information
    name='thecut-durationfield',
    version=__version__,

    # Packaging
    packages=find_packages(exclude=['docs']),
    namespace_packages=['thecut'],
    include_package_data=True,

    # Dependencies
    install_requires=[
        'isodate >= 0.5',
        'python-dateutil >= 2.2'
    ],
    # Author information
    author='The Cut Creative',
    author_email='development@thecut.net.au',

    # Additional information
    url='https://projects.thecut.net.au/projects/thecut-durationfield',
    license='Apache Software License 2.0',
    description=('Form and model fields for storing durations on Django '
                 'models as ISO 8601 compliant strings, and returning '
                 'relativedelta objects.'),
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
)
