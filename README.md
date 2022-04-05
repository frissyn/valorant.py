# valorant.py

[![Actions](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Ffrissyn%2Fvalorant.py%2Fbadge%3Fref%3Dmaster&style=flat-square)](https://actions-badge.atrox.dev/frissyn/valorant.py/goto?ref=master)
[![PyPI](https://img.shields.io/pypi/v/valorant?style=flat-square)](https://pypi.python.org/pypi/valorant)
[![Downloads](https://img.shields.io/pypi/dm/valorant?style=flat-square)](https://pepy.tech/project/valorant)
![LICENSE](https://img.shields.io/github/license/frissyn/valorant.py?style=flat-square)
[![Discord](https://img.shields.io/badge/discord-join-7389D8?style=flat-square&logo=discord)](https://discord.gg/b3qjk4epPr)

`valorant.py` is an unofficial API wrapper for Riot Games' Valorant API endpoints. It's modern, easy to use, feature-rich, and intuitive!

## Features

+ **Simple:** High-level abstraction of API interactions; easy to use and easy to customize.

+ **Lightweight:** Doesn't rely on any external dependencies, minimal package size.

+ **Extensive:** Covers all Valorant related endpoints from the Riot Games API. Also includes Account coverage.

+ **Fast:** HTTP requests and object instancing optimized to use minimal resources and complete tasks quickly!

+ **Intuitive:** Complete auto-completion, docstrings, and type-hinting for all library objects and variables.

## Installation

`valorant.py` requires Python 3.8 or higher.

|Manager     |Command                  |
|:----------:|:------------------------|
|PIP         |`pip install valorant`   |
|Poetry      |`poetry add valorant`    |

## Usage

Take a look at the [`examples/`](https://github.com/frissyn/valorant.py/blob/master/examples) folder for more usage snippets!

**Quickstart:**

```python
import valorant

KEY = "RGAPI-Key-Here"
client = valorant.Client(KEY)

agents = client.get_characters()

print(agents.get("Viper"))
```

**Local Client:**

```python
import valorant

client = valorant.LocalClient()

print(client.get_session())
```

**NOTE:** *The Local Client interacts with the Client API that Valorant uses while the game is running on your system. This means access to current player, friend requests, shop, etc. The Local Client is currently unstable. `valorant.py` is not liable for any punishment you may recieve should you use its tools to break Valorant ToS. (i.e Auto-Agent Selection)*

## Documentation

The public API documentation for `valorant.py` is hosted on [ReadTheDocs.io](https://valorantpy.readthedocs.io/en/latest/).

Use `bash bin/docs` to start the documentation server locally. This uses Ruby's `WEBrick` gem.

## Help and Questions

Have a bug or issue? Need help with the API? Open an [issue](https://github.com/frissyn/valorant.py/issues) or hop in the [#valorant-py](https://discord.gg/b3qjk4epPr) channel of the Frisscraft Community Discord Server.

## Contributing

Head over to the [**Contributing Guide**](https://github.com/frissyn/valorant.py/blob/master/.github/CONTRIBUTING.md) page.