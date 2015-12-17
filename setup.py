import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()


setup(
    name="yamlconf",
    version="0.1.0",  # Update in yamlconf/__init__.py too
    author="Aaron Halfaker",
    author_email="ahalfaker@wikimedia.org",
    description=("This library provides a means to read yaml configuration " +
                 "files and propagate default values in reasonable ways.  " +
                 "Nothing complicated."),
    license="MIT",
    url="https://github.com/halfak/yamlconf",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=['pyyaml'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
