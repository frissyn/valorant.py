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

| \_\_init\_\_(*obj*)| Initialize the `Client` object.                                   |
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

`client.get_user(value, via="puuid")` returns a user via a given method. Valid `via` values are `puuid` and `name`. If `via` equals `puuid`, the client will get the Account DTO by puuid. If `via` equals `name`, the client will get the Account DTO by gameName and tagLine split by a delimiter (e.g `IreTheKID#0000`).

## Reloading

Upon initilalizing the `Client`, if `reload=True` the Client will cache a reponse from the **VAL-CONTENT-V1** endpoint. This will not be updated until you call `client.reload()`. If `reload=False` the Client will not cache a response, and you'll have to call it yourself. This is because, in my experience, you'll make requests to the Content endpoint the most often, which can easily lead you to a `429` HTTP error. `client.reload()` exists to mitigate that risk. However, getting users and platform_status will make a call to the API everytime. This is because the data from these requests change the most frequently, and getting up-to-date information is a lot more important in more contexts than the Content endpoint.

## Custom Requests

As of version `0.1.8`, you can build custom requests to the API instead of being limited to the request methods that the `Client` provides by default. This isn't a normal feature for most API wrappers, but considering how locked down the Valorant API is, it makes sense that you might need to customize your requests to fit your use case.

Start by passing an empty API Key string and setting `reload` to `False`:

```python
client = valorant.Client("", reload=False)
```

From there you can do two things: build a header, or build a URL (likely both). From the `values` module you can view all the valid endpoints, reigons, routes, etc. to build your URLs to make a request to. Then using the `client.fetch()` method, which is a copy of the `requests.get()` method, you can make your request. Here's a complete example:

```python
import os
import random

from valorant import Client
from valorant.values import ENDPOINTS, REIGONS

KEY = os.environ["KEY"]
client = Client("", reload=False)

h = client.build_header({"X-Riot-Token": KEY})
url = client.build_url(code=random.choice(REIGONS), endpoint="content")

content = client.fetch(url, headers=h)

print(content)
```

The complete list of valid values can be found in the `.values` module. This includes routes, reigons, endpoints, URLs, etc.