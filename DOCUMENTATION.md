# Documentation

This documentation closely mimics what you would find in Riot Games' Official Docs for the Valorant API. This is on purpose, to make it easier to integrate valorant.py into your application; you won't have to constantly look between two different docs. (*Currently, there is only functionality for the **VAL-CONTENT-V1** and **VAL-STATUS-V1** endpoint.*)

### Quickstart 

```python
import os
import valorant

API_KEY = os.getenv("API_KEY")
client = valorant.Client(API_KEY)

agents = client.get_characters()

for agent in agents:
	print(agent.name, agent.id)
```

### Classes

`valorant.Client(apiKey, locale)`

| Parameter | Type   | Description                                                                                                    |
|-----------|--------|----------------------------------------------------------------------------------------------------------------|
| apiKey    | string | Your API Key provided by Riot Games. All keys work regardless of access type.                                  |
| locale    | string | A standard locale string containing language and region (i.e "en-US"). Defaults to [`locale.get_locale()[0]`](https://docs.python.org/3/library/locale.html#locale.getlocale) |

### Functions

| Functions                      | Description                         |
|:-------------------------------|:------------------------------------|  
| `client.reload()`              | Refreshes client content.           |
| `client.get_acts()`            | Returns a list of `ActDTO`s         |
| `client.get_characters()`      | Returns a list of `ContentItemDTO`s |
| `client.get_maps()`            | Returns a list of `ContentItemDTO`s |
| `client.get_chromas()`         | Returns a list of `ContentItemDTO`s |
| `client.gets_skins()`          | Returns a list of `ContentItemDTO`s |
| `client.get_skin_levels()`     | Returns a list of `ContentItemDTO`s |
| `client.get_equips()`          | Returns a list of `ContentItemDTO`s |
| `client.get_game_modes()`      | Returns a list of `ContentItemDTO`s |
| `client.get_sprays()`          | Returns a list of `ContentItemDTO`s |
| `client.get_spray_levels()`    | Returns a list of `ContentItemDTO`s |
| `client.get_charms()`          | Returns a list of `ContentItemDTO`s |
| `client.get_charm_levels()`    | Returns a list of `ContentItemDTO`s |
| `client.get_player_cards()`    | Returns a list of `ContentItemDTO`s |
| `client.get_player_titles()`   | Returns a list of `ContentItemDTO`s |
| `client.get_platform_status()` | Returns a `PlatformDataDTO`         |
| `client.get_user(value, via="puuid")` | Returns an `AccountDTO`      |

`client.get_user(value, via="puuid")`:

Returns a user via a given method. Valid `via` values are `puuid` and `name`. If `via` equals `puuid`, the client will get the Account DTO by puuid. If `via` equals `name`, the client will get the Account DTO by gameName and tagLine split by a delimiter (e.g `IreTheKID#0000`).


### Objects

`valorant.dto.ActDTO`

| Attribute      | Type | Description                                        |
|:---------------|:-----|:---------------------------------------------------|
| name           | str  |                                                    |
| localizedNames | dict | This attribute is omitted if a locale is provided. |
| id             | str  |                                                    |
| isActive       | bool |                                                    |

`valorant.dto.ContentItemDTO`

| Attribute      | Type | Description                                          |
|:---------------|:-----|:-----------------------------------------------------|
| name           | str  |                                                      |
| localizedNames | dict | This attribute is omitted if a locale is provided.   |
| id             | str  |                                                      |
| assetName      | str  |                                                      |
| assetPath      | str  | This attribute only appears for maps and game modes. |

`valorant.dto.PlatformDataDTO`

| Attribute      | Type              | Description   |
|:---------------|:------------------|:--------------|
| id             | str               |               |
| name           | str               |               |
| locales        | list[str]         |               |
| maintenances   | list[dict]        |               |
| incidents      | list[dict]        |               |


`valorant.dto.AccountDTO`

| Attribute      | Type | Description                                        |
|:---------------|:-----|:---------------------------------------------------|
| puuid          | str  |                                                    |
| gameName       | str  | This attribute may be `None`.                      |
| tagLine        | str  | This attribute may be `None`.                      |