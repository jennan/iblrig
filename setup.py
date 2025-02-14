from setuptools import setup, find_packages
import sys
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent.absolute()

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of iblrig requires Python {}.{}
Environment Python version =  {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    require = [x.strip() for x in f.readlines()]

setup(
    name='iblrig',
    version='6.0.5',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    description='IBL libraries',
    license="MIT",
    long_description=long_description,
    author='IBL Staff',
    url="https://www.internationalbrainlab.com/",
    packages=find_packages(exclude=['scratch']),  # same as name
    # external packages as dependencies
    install_requires=require,
    scripts={

    }
)
