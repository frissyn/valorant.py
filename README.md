# valorant.py

[![GitHub Actions](https://camo.githubusercontent.com/0fc9226929794d4d4dfb9ac05a1786942f8e4b4300207224277ac49e22e9fdb6/68747470733a2f2f7472617669732d63692e636f6d2f7073662f626c61636b2e7376673f6272616e63683d6d6173746572)](https://github.com/IreTheKID/valorant.py/actions)
[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/IreTheKID/valorant.py/issues)

A synchronous client package for interacting with Riot Games' Valorant API endpoints. This is currently under a lot of construction, more stuff coming soon!

### Installation

**pip**: `pip install valorant`

**poetry**: `python3 -m poetry add valorant`

### Usage

Quickstart Guide:
```python
import os
import valorant

API_KEY = os.getenv("API_KEY")
client = valorant.Client(KEY)

agents = client.get_characters()

for agent in agents:
	print(agent.name)
```

### Documentation

[**valorant.py Documentation**](https://github.com/IreTheKID/valorant.py/blob/master/DOCUMENTATION.md)
