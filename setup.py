import re
from os import path
from setuptools import setup


# read() and find_version() taken from jezdez's python apps, ex:
# https://github.com/jezdez/django_compressor/blob/develop/setup.py

def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-automotive',
    version=find_version('automotive', '__init__.py'),
    author='Massimo Scamarcia',
    author_email='massimo.scamarcia@gmail.com',
    description="Simple automotive models and data for Django projects.",
    long_description=read('README.md'),
    url='https://github.com/mscam/django-automotive/',
    license='UNLICENSE',
    packages=[
        'automotive',
        'automotive.fixtures',
        'automotive.migrations',
        'automotive.south_migrations',
    ],
    package_data = {
        'automotive.fixtures': ['*.json',],
    },
    install_requires=['Django>=1.5', 'django-autoslug'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.2",
        # "Programming Language :: Python :: 3.3",
        # "Programming Language :: Python :: 3.4",
        'Topic :: Utilities',
        "Framework :: Django",
    ]
)
