## Source

[`valorant/objects.py`](https://github.com/frissyn/valorant.py/blob/master/valorant/objects.py)

## Quickstart

```python
import valorant

KEY = "RGAPI-Key-Goes-Here"
client = valorant.Client(KEY, reigon="na")

modes = client.get_game_modes()
skins = client.get_chromas()

print(modes.get("Deathmatch"))

for s in skins:
    n = s.name
    if "Vandal" in n and "Level" not in n:
        print(n)
```

## Overview

The Valorant API, along with almost all of Riot's APIs use Data Transfer Objects: Containers of data that have no behavioral qualities except to be self-aware. (Not in the sentient way, of coure =P). The API wrapper reads these DTOs from a JSON format and turns them into Python objects where dictionary key names become attribute names.

Because these objects do almost nothing more than mimic the DTOs you'd get from the API, you don't have to look between the `valorant.py` docs and the Official Valorant API docs. (Hopefully.) Sticking to one or the other should do the job nicely.

## Objects

All DTOs (in `valorant.py`) inherit from the same DTO class; they have different names for the sake of semantics and debugging. There are also other objects that have different purposes, such as `ContentList` which is functionally the same as a Python `list`, but with a safe `get` method for getting DTOs in the list by name. Here's a list of them all:

#### AccountDTO

| Attribute      | Type | Description                                        |
|:---------------|:-----|:---------------------------------------------------|
| puuid          | str  |                                                    |
| gameName       | str  | This attribute may be `None`.                      |
| tagLine        | str  | This attribute may be `None`.                      |


#### ActDTO

| Attribute      | Type   | Description                                        |
|:---------------|:-------|:---------------------------------------------------|
| name           | `str`  |                                                    |
| localizedNames | `dict` | This attribute is omitted if a locale is provided. |
| id             | `str`  |                                                    |
| isActive       | `bool` |                                                    |


#### ContentItemDTO

| Attribute      | Type   | Description                                          |
|:---------------|:-------|:-----------------------------------------------------|
| name           | `str`  |                                                      |
| localizedNames | `dict` | This attribute is omitted if a locale is provided.   |
| id             | `str`  |                                                      |
| assetName      | `str`  |                                                      |
| assetPath      | `str`  | This attribute only appears for maps and game modes. |


#### LeaderboardDTO

| Attribute      | Type         | Description                                          |
|:---------------|:-------------|:-----------------------------------------------------|
| shard          | `str`        | The shard for the given leaderboard.                 |
| actId          | `str`        | The Act ID for the given leaderboard.                |
| totalPlayers   | `int`        | Total number of players on the given leaderboard.    |
| players        | `ContentList`| `ContentList` of `PlayerDTO`s                        |


#### PlatformStatusDTO

| Attribute      | Type                | Description                                |
|:---------------|:--------------------|:-------------------------------------------|
| id             | `str`               |                                            |
| name           | `str`               |                                            |
| locales        | `list[str]`         | List of all valid locales.                 |
| maintenances   | `list[dict]`        | List of maintenances (Fixes, Updates, etc.)|
| incidents      | `list[dict]`        | List of incidents (Bugs, Issues, etc.)     |


#### PlayerDTO

| Attribute       | Type                | Description                                |
|:----------------|:--------------------|:-------------------------------------------|
| puuid           | `str`               |                                            |
| gameName        | `str`               |                                            |
| tagLine         | `str`               |                                            |
| leaderboardRank | `int`               |                                            |
| rankedRating    | `int`               |                                            |
| numberOfWins    | `int`               |                                            |

#### ContentList

*ContentList is a subclass of the base `list` class in Python. Besides these listed methods, anything you can do with a list you can do with a ContentList as well.*

|Method                     |Description                                                                  |
|:--------------------------|:----------------------------------------------------------------------------|
|`get(name, default=None)`  |Gets a DTO in the list by `name` attribute. Returns `default` if not found.  |
|`find(value, attr="name")` |Find an item in the ContentList by a given attribute value.                  |
