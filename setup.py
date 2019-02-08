import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyroutelib2",
    version="0.1.0",
    author="Mark Torok",
    author_email="torokm@starschema.net",
    description="This package is a fork of the original pyroutelib2 repo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/torokmstar/pyroutelib2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.5",
        "License :: OSI Approved :: ",
        "Operating System :: OS Independent",
    ],
)
