# `cdncheck-python`

[![Tests](https://github.com/blacklanternsecurity/cdncheck-python/actions/workflows/tests.yml/badge.svg?branch=stable)](https://github.com/blacklanternsecurity/cdncheck-python/actions?query=workflow%3A"tests")

This is a Python wrapper around ProjectDiscovery's [cdncheck](https://github.com/projectdiscovery/cdncheck). It is useful for checking whether a given IP address belongs to a cloud provider, e.g. Google, Azure, etc. 

Tests are run on a weekly schedule.

## Installation
If you run into problems with installation, please make sure golang is installed on your system.
```bash
$ pip install cdncheck
```

## Usage (CLI)
```bash
$ cdncheck 1.2.3.4
1.2.3.4 does not belong to a CDN

$ cdncheck 168.62.20.37
168.62.20.37 belongs to CDN "azure"
```

## Usage (Python)
```python
>>> from cdncheck import cdncheck
# empty string == not belonging to a CDN
>>> cdncheck('1.2.3.4')
''
>>> cdncheck('168.62.20.37')
'azure'
```
