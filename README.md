# valorant.py

[![GitHub Actions](https://camo.githubusercontent.com/0fc9226929794d4d4dfb9ac05a1786942f8e4b4300207224277ac49e22e9fdb6/68747470733a2f2f7472617669732d63692e636f6d2f7073662f626c61636b2e7376673f6272616e63683d6d6173746572)](https://github.com/frissyn/valorant.py/actions)
[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Downloads](https://pepy.tech/badge/valorant/month)](https://pepy.tech/project/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/frissyn/valorant.py/issues)
[![Discord Chat](https://img.shields.io/badge/discord-join-7389D8?style=flat&logo=discord)](https://discord.gg/b3qjk4epPr)

`valorant.py` is an unofficial API wrapper for Riot Games' Valorant API endpoints. It's modern, easy to use, feature-rich, and intuitive!

## Features

**Simple:** High-level abstraction of API interactions; easy to use and easy to customize.

**Lightweight:** Doesn't rely on any external dependencies, minimal package size.

**Extensive:** Covers all Valorant related endpoints from the Riot Games API. Also includes Account coverage.

**Fast:** HTTP requests and object instancing optimized to use minimal resources and complete tasks quickly!

**Intuitive:** Complete auto-completion, docstrings, and type-hinting for all library objects and variables.

## Installation

`valorant.py` requires Python 3.8 or higher.

|Manager     |Command                  |
|:----------:|:------------------------|
|PIP         |`pip install valorant`   |
|Poetry      |`poetry add valorant`    |
|PIPEnv      |`pipenv install valorant`|

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

Have a bug or issue? Need help with the API? Open an [issue](https://github.com/frissyn/valorant.py/issues) or hop in the [#valorant-py](https://discord.gg/b3qjk4epPr) channel of my Community Discord Server.

## Contributing

1. Fork the repository: [`Fork`](https://github.com/frissyn/valorant.py/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -a -m 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request! 🎉

You can also re-create these steps with GitHub Desktop, Visual Studio Code, or whatever `git` version control UI you prefer. You don't have to, but I use prefixes for all my commits (i.e `✨: add asyncio run to package namespace`). I have a personal style guide that I use, which you can find [`here`](https://github.com/frissyn/commit-prefixes).
