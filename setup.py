from setuptools import setup, find_packages
from sys import platform

# read the contents of the README file
import os
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# function to recursively get files for resourcee
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


# get all files recursively from /resources
resource_files = package_files('./resources')

setup(
    name="medspacy-ssi",
    version="0.0.0.1",
    description="Library for clinical NLP with spaCy.",
    author="Alec Chapman",
    author_email="alec.chapman@hsc.utah.edu",
    packages=find_packages(),
    install_requires=[
        # NOTE: spacy imports numpy to bootstrap its own setup.py in 2.3.2
        "medspacy>=0.1.0.2"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"medspacy_ssi": resource_files},
)