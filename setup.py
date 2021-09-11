from setuptools import setup, find_packages
import io
import os

VERSION = "0.0.0"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="confluence-to-sqlite",
    description="CLI tool for loading data from a Confluence instance into a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ryan Cheley",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=["sqlite-utils", "click"],
    extras_require={"test": ["pytest"]},
    tests_require=["confluence-to-sqlite[test]"],
    setup_requires=["pytest-runner"],
    entry_points="""
        [console_scripts]
        confluence-to-sqlite=confluence_to_sqlite.cli:cli
    """,
    url="https://github.com/ryancheley/confluence-to-sqlite",
    project_urls={
        "Issues": "https://github.com/ryancheley/confluence-to-sqlite/issues",
        "CI": "https://github.com/ryancheley/confluence-to-sqlite/actions",
        "Changelog": "https://github.com/ryancheley/confluence-to-sqlite/releases",
    },
    python_requires=">=3.6",
)