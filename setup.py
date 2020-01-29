import re
from pathlib import Path
import setuptools


def getLongDescription():
    with open("README.md", "r") as fh:
        longDescription = fh.read()
    return longDescription


def getRequirements():
    requirements = []
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
    return requirements


def getVersion():
    path = Path(__file__).parent.resolve() / "beepboop.py"
    with open(path, "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if not version_match:
        raise RuntimeError("Unable to find version string.")
    version = version_match.group(1)
    return version


setuptools.setup(
    name="beepboop",
    version=getVersion(),
    author="Natalie Fearnley",
    author_email="nfearnley@gmail.com",
    description="Example Cog",
    long_description=getLongDescription(),
    long_description_content_type="text/markdown",
    url="https://github.com/nfearnley/beepboop",
    python_requires=">=3.7",
    install_requires=getRequirements(),
    py_modules=["beepboop"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)
