from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdf-document-processor",
    version="1.1.0",
    description="A utility for merging and organizing PDF documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Malek Elaghel",
    author_email="malekelaghel@gmail.com",
    url="https://github.com/it-malek/pdf-merge-utility",
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'pypdf>=3.0.0',
    ],
    python_requires=">=3.7",
    # Add this for better package discovery
    package_data={
        "": ["LICENSE", "README.md"],
    },
    # Add this for command-line usage
    entry_points={
        "console_scripts": [
            "pdf-processor=src.main:main",
        ],
    },
)
