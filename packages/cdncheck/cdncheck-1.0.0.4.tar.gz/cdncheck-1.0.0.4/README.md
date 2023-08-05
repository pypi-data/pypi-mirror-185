# `cdncheck-python`

This is a Python wrapper around ProjectDiscovery's [cdncheck](https://github.com/projectdiscovery/cdncheck). Given an IP address it will identify which cloud provider, if any, it belongs to.

## Installation
```bash
$ pip install cdncheck
```

## Usage (CLI)
```bash
$ cdncheck 1.2.3.4
1.2.3.4 does not belong to a CDN

$ cdncheck 168.62.20.37
168.62.20.37 belongs to CDN azure
```

## Usage (Python)
```python
>>> from cdncheck import cdncheck
>>> cdncheck.cdncheck('1.2.3.4')
''
>>> cdncheck('168.62.20.37')
'azure'
```
