# Python API

### Overview

- **Description:** This repository contains code for the [Python API](https://pypi.org/project/coda-api/) to the CODA platform. This library is aimed at facilitating use of the CODA platform when it is used from the [notebook app](https://github.com/coda-platform/notebook-app). 
- **Primary author(s):** Louis Mullie [[@louism](https://github.com/louismullie)].
- **Contributors:** None.
- **License:** The code in this repository is released under the GNU General Public License, V3.

### Publishing

```
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```