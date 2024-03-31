from setuptools import find_packages, setup

setup(
    name="common-library",
    version="0.0.1",
    description="common library",
    url="https://github.com/common-library/python",
    long_description="",
    long_description_content_type="text/markdown",
    author="heaven-chp",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
)
