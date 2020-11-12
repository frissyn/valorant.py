# valorant.py

[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
