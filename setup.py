import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Developers",
    author_email="developers@pinaxproject.com",
    description="RESTful API adhering to the JSON API specification",
    name="pinax-api",
    long_description=read("README.md"),
    version="0.1.0",
    url="http://github.com/pinax/pinax-api/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "api": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "django-appconf>=1.0.1",
        "mock>=2.0.0",
    ],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
