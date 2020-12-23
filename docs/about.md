# valorant.py

[![GitHub Actions](https://camo.githubusercontent.com/0fc9226929794d4d4dfb9ac05a1786942f8e4b4300207224277ac49e22e9fdb6/68747470733a2f2f7472617669732d63692e636f6d2f7073662f626c61636b2e7376673f6272616e63683d6d6173746572)](https://github.com/IreTheKID/valorant.py/actions)
[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Downloads](https://pepy.tech/badge/valorant)](https://pepy.tech/project/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/IreTheKID/valorant.py/issues)

An unofficial synchronous client package for interacting with Riot Games' Valorant API endpoints. 

### Installation

**pip**: `pip install valorant`

**easy_install**: `easy_install valorant`

**poetry**: `python -m poetry add valorant`

### Usage

Quickstart Guide:
```python
import os
import valorant

API_KEY = os.getenv("API_KEY")
client = valorant.Client(API_KEY)

agents = client.get_characters()

for agent in agents:
	print(agent.name)
```

### Documentation

[**valorant.py Documentation**](https://valorantpy.repl.co/docs.html)

### Contributing

Contributions are always welcome! There currently isn't a contribution guide, but bug reports, additional endopint coverage, and other fun stuff is always welcome in [issues](https://github.com/IreTheKID/valorant.py/issues)!
