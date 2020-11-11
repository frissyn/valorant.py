# valorant.py

A synchronous client package for interacting with Riot Games' Valorant API endpoints. This is currently under a lot of construction, more stuff coming soon!

### Installation

**pip**: `pip install valorant`

**poetry**: `python3 -m poetry add valorant`

### Usage

Quickstart Guide:
```python
import os
import json
import valorant

API_KEY = os.environ["API_KEY"]

client = valorant.Client(API_KEY)

print(json.dumps(client.characters, indent=2))
```
