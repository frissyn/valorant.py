# valorant.py

[![GitHub Actions](https://camo.githubusercontent.com/0fc9226929794d4d4dfb9ac05a1786942f8e4b4300207224277ac49e22e9fdb6/68747470733a2f2f7472617669732d63692e636f6d2f7073662f626c61636b2e7376673f6272616e63683d6d6173746572)](https://github.com/frissyn/valorant.py/actions)
[![valorant on PyPI](https://img.shields.io/pypi/v/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Downloads](https://pepy.tech/badge/valorant/month)](https://pepy.tech/project/valorant)
[![License](https://img.shields.io/pypi/l/valorant.svg)](https://pypi.python.org/pypi/valorant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contribute](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/frissyn/valorant.py/issues)

`valorant.py` is an unofficial API wrapper for Riot Games' Valorant API endpoints. It's modern, easy to use, feature-rich, and intuitive! Implemented with object oriented designs and explicit reloads to prevent `429`s, valorant.py is the best Valorant API wrapper out there!

## Bulletin Board

**Most recent version:** `0.5.0` (🎉)

**Changes:**

+ Internal redesign of HTTP requests
+ Updates to error handling for Client and AsyncClient
+ A few bug fixes (👍)
+ *References:* [#24](https://github.com/frissyn/valorant.py/issues/24), [#20](https://github.com/frissyn/valorant.py/issues/20), [#23](https://github.com/frissyn/valorant.py/issues/23)

**Coming Soon:** Endpoint coverage for matches!

## Installation

|Manager|Command|
|:-:|:--|
|PIP|`pip install valorant`|
|Poetry|`python -m poetry add valorant`|
|Easy Install|`easy_install valorant`|

## Usage

Quickstart:

```py
import valorant

KEY = "RGAPI-Key-Here"
client = valorant.Client(KEY)

agents = client.get_characters()

for agent in agents:
    print(agent.name)
```

Asynchronous Client:

```py
import valorant

KEY = "RGAPI-Key-Here"
client = valorant.AsyncClient(KEY)

async def _main():
    agents = await client.get_characters()

    for agent in agents:
        print(agent.name)

valorant.run(_main())
```

Local Client:

*This is intended for use with the game locally. Eases the use of doing things like getting live match data, chat sessions, friend requests, etc. Doesn't need an access key. The current Local Client is a work-in-progress and is unstable.*

```python
import valorant

client = valorant.LocalClient()

print(client.get_session())
```

## Documentation

The public API documentation for `valorant.py` is hosted [`here`](https://valorantpy.readthedocs.io/en/latest/).

If you're making edits to the documentation, you can generate the HTML and start a local server by running `bash bin/docs.sh` in the repository directory. This requires [`Ruby`](https://www.ruby-lang.org/en/documentation/installation/) 2.5 or higher (Sorry if you have to install Ruby just to edit the docs =P).

## Contributing

1. Fork the repository: [`Fork`](https://github.com/frissyn/valorant.py/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -a -m 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request! 🎉

You can also re-create these steps with GitHub Desktop, Visual Studio Code, or whatever `git` version control UI you prefer. You don't have to, but I use prefixes for all my commits (i.e `✨: add asyncio run to package namespace`). I have a personal style guide that I use, which you can find [`here`](https://github.com/frissyn/commit-prefixes).


## Final Note

**Thanks for taking the time to check out `valorant.py`! 🎉**
