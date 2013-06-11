from setuptools import setup, find_packages
from version import get_git_version

setup(name='thecut-durationfield',
    author='The Cut', author_email='development@thecut.net.au',
    url='http://projects.thecut.net.au/projects/thecut-durationfield',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['distribute', 'isodate == 0.4.9',],
)
