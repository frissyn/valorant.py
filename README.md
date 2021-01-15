# valorant.py

[![GitHub Actions](https://camo.githubusercontent.com/0fc9226929794d4d4dfb9ac05a1786942f8e4b4300207224277ac49e22e9fdb6/68747470733a2f2f7472617669732d63692e636f6d2f7073662f626c61636b2e7376673f6272616e63683d6d6173746572)](https://github.com/IreTheKID/valorant.py/actions)
[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Downloads](https://pepy.tech/badge/valorant/month)](https://pepy.tech/project/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/IreTheKID/valorant.py/issues)

valorant.py is an unofficial API wrapper for Riot Games' Valorant API endpoints. It's modern, easy to use, feature-rich, and intuitive! Implemented with object oriented designs and explicit reloads to prevent `429`s, valorant.py is the best Valorant API wrapper out there!

### Installation

**pip**: `pip install valorant`

**easy_install**: `easy_install valorant`

**poetry**: `python -m poetry add valorant`

### Usage

Quickstart Guide:
```python
import valorant

KEY = "RGAPI-Key-Goes-Here"
client = valorant.Client(KEY, locale=None)

maps = client.get_maps()
agents = client.get_characters()

print(agents.get("Viper"))
print(maps.get("Ascent"))
```

### Documentation

[**valorant.py Documentation**](https://github.com/IreTheKID/valorant.py/tree/master/docs)

### Contributing

Contributions are always welcome! There currently isn't a contribution guide, but bug reports, additional endopint coverage, and other fun stuff is always welcome in [issues](https://github.com/IreTheKID/valorant.py/issues)!

### TO-DO

**Work in Progress:**
+ Add an Asynchronous Client
+ Add coverage for **VAL-MATCH** endpoint

**To be Worked On:**
+ Fully cover **VAL-STATUS** endpoint
+ Add customizable rate-limits
