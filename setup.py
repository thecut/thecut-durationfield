from __future__ import print_function
import codecs
import io
import os
from thecut.exampleapp import __version__
from setuptools import setup, find_packages
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'HISTORY.rst')

setup(
    # General information
    name='thecut-exampleapp',
    version=__version__,

    # Packaging
    packages=find_packages(exclude=['docs']),
    namespace_packages=['thecut'],
    include_package_data=True,

    # Dependencies
    install_requires=['sphinx_rtd_theme>=0.1.10a0'],

    # Author information
    author='The Cut Creative',
    author_email='development@thecut.net.au',

    # Additional information
    url='https://projects.thecut.net.au/projects/thecut-exampleapp',
    license='Apache Software License 2.0',
    description='A reusable application.',
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
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
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
)
