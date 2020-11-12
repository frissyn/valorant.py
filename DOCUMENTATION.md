# Documentation

This documentation closely mimics what you would find in Riot Games' Official Docs for the Valorant API. This is on purpose, to make it easier to integrate valorant.py into your application; you won't have to constantly look between two different docs. (*Currently, there is only functionality for the **VAL-CONTENT-V1** endpoint.*)

### Quickstart 

```python
import os
import json
import valorant

API_KEY = os.getenv("API_KEY")
client = valorant.Client(API_KEY)

agents = client.get_agents()

for agent in agents:
	print(agent.name, agent.id)
```

### Classes

`valorant.Client(apiKey, locale)`

| Parameter | Type   | Description                                                                                                    |
|-----------|--------|----------------------------------------------------------------------------------------------------------------|
| apiKey    | string | Your API Key provided by Riot Games. All keys work regardless of access type.                                  |
| locale    | string | A standard locale string containing language and region (i.e "en-US"). Defaults to your region's default locale. Can also be `None`. |

### Functions

| Functions                    | Description                         |
|:-----------------------------|:------------------------------------|  
| `client.reload()`            | Refreshes client content.           |
| `client.get_acts()`          | Returns a list of `ActDto`s         |
| `client.get_characters()`    | Returns a list of `ContentItemDto`s |
| `client.get_maps()`          | Returns a list of `ContentItemDto`s |
| `client.get_chromas()`       | Returns a list of `ContentItemDto`s |
| `client.gets_skins()`        | Returns a list of `ContentItemDto`s |
| `client.get_skin_levels()`   | Returns a list of `ContentItemDto`s |
| `client.get_equips()`        | Returns a list of `ContentItemDto`s |
| `client.get_game_modes()`    | Returns a list of `ContentItemDto`s |
| `client.get_sprays()`        | Returns a list of `ContentItemDto`s |
| `client.get_spray_levels()`  | Returns a list of `ContentItemDto`s |
| `client.get_charms()`        | Returns a list of `ContentItemDto`s |
| `client.get_charm_levels()`  | Returns a list of `ContentItemDto`s |
| `client.get_player_cards()`  | Returns a list of `ContentItemDto`s |
| `client.get_player_titles()` | Returns a list of `ContentItemDto`s |

### Objects

`valorant.dto.ActDto`

| Attribute      | Type | Description                                        |
|:---------------|:-----|:---------------------------------------------------|
| name           | str  |                                                    |
| localizedNames | dict | This attribute is omitted if a locale is provided. |
| id             | str  |                                                    |
| isActive       | bool |                                                    |

`valorant.dto.ContentItemDto`

| Attribute      | Type | Description                                          |
|:---------------|:-----|:-----------------------------------------------------|
| name           | str  |                                                      |
| localizedNames | dict | This attribute is omitted if a locale is provided.   |
| id             | str  |                                                      |
| assetName      | str  |                                                      |
| assetPath      | str  | This attribute only appears for maps and game modes. |
