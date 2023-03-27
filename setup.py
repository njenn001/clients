import os
import sys 
from setuptools import setup
import distutils.core
from distutils.command.install import install

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "TC Speech Analyzer",
    version = "0.0.0",
    author = "Noah Jennings",
    author_email = "ntjennings1@odu.edu",
    description = ("TKinter GUI to capture and label speech data."),
    license = "MIT",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['flaskr', 'tests'],
    long_description=read('README.md')
)
