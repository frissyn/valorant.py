## Source

[`valorant/client.py`](https://github.com/IreTheKID/valorant.py/blob/master/valorant/client.py)

## Quickstart

```python
import os
import valorant

KEY = os.environ["KEY"]
client = valorant.Client(KEY, locale=None)
```

## Initialize

| \_\_init\_\_(*obj*)| Initialize the `Client` object.                                    |
|:-------------------|:------------------------------------------------------------------|

| Parameters  |                 |                                                        |
|:------------|:----------------|:-------------------------------------------------------|
| key         | `str` or `None` | Your given RGAPI key. Can be any access-level.         |
| locale      | `str` or `None` | A standard locale string containing language and region (i.e "en-US"). Defaults to [`locale.get_locale()[0]`]()|
| region      | `str`           | Valid API reigon string. (i.e `na` or `eu`). Defaults to `na`|
| route       | `str`           | Valid API region route  string. (i.e `americas`). Defaults to `americas`|
| reload      | `bool`          | Whether to load client content on initialization. Defaults to `True`|

## Functions

The valorant `Client` object has a number of **get** functions for retrieving information from the **VAL-CONTENT-V1** endpoint. They are named in conjunction with Riot's own documentation. For example, getting Valorant Agents would look like this:

```python
agents = client.get_characters()
```

All Valorant content can be retrieved with `get_<data>()` where **data** is the name of the content in *snake_case*. These functions return a [`ContentList`](https://github.com/IreTheKID/valorant.py/blob/master/valorant/dto.py#L50), which is a standard Python list with an added `get` method for getting DTOs by *name*. Returns `None` if no item in the list has the given name.

```python
viper = agents.get("Viper") # Returns a ContentItemDTO
oops = agents.get("Shadow") # Returns None
```

