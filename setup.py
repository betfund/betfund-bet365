"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="betfund-bet365",
    version="0.0.6",
    description="High Throughput Wrapper for Bet365 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/betfund/betfund-bet365",
    author="Michell Bregman, Leon Kozlowski",
    author_email="mitchbregs@gmail.com, leonkozlowski@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="betfund lines bet365",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    extras_require={
        "testing": [
            "black",
            "flake8",
            "mock",
            "pylint",
            "pytest",
            "pytest-cov"
        ]
    }
)