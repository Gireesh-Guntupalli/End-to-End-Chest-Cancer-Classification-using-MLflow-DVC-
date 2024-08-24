# setup.py
# The setup.py file is the build script for setuptools, a Python tool used to package and distribute Python projects. It contains metadata about the package (such as name, version, author, dependencies, etc.) and defines how the package should be installed.

# The Purpose
# Together, these two files (requirements.txt with -e . and setup.py) work as follows:

# Development Environment: When you run pip install -r requirements.txt, the -e . ensures that the package in the current directory is installed in editable mode. This is useful during development because any changes you make to the code will be reflected immediately without needing to reinstall the package.
# setup.py as Source of Truth: The setup.py file defines the package metadata and dependencies. When you install the package with -e ., it uses this file to know how to structure and install the package, including its dependencies.
# Editable Installation: With an editable installation, you can modify your source code and immediately test those changes without needing to reinstall the package, which streamlines development and debugging.
# This setup is common in Python projects where you are actively developing or contributing to a package.

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
