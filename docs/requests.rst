Requests
========

As of version ``0.1.8``, you can build custom requests to the API
instead of being limited to the request methods that the ``Client``
provides by default. This isn't a normal feature for most API wrappers,
but considering how locked down the Valorant API is, it makes sense that
you might need to customize your requests to fit your use case.

Start by passing an empty API Key string and setting ``reload`` to
``False``:

.. code:: python

   client = valorant.Client(None, reload=False)

From there you can do two things: build a header, or build a URL (likely
both). From the ``values`` module, where you can view all the valid
endpoints, reigons, routes, etc. to build your URLs to make a request
to. Then using the ``client.fetch()`` method, which is a copy of the
``requests.get()`` method, you can make your request. The following
example will build the request headers and select a random region to
build the URL with:

.. code:: python

   import random

   from valorant import Client
   from valorant.values import ENDPOINTS, REIGONS

   KEY = "RGAPI-Key-Goes-Here"
   client = Client(None, reload=False)

   h = client.build_header({"X-Riot-Token": KEY})
   url = client.build_url(code=random.choice(REIGONS), endpoint="content")

   content = client.fetch(url, headers=h)

   print(content)

The complete list of valid values can be found in the ```.values```_
module. This includes routes, reigons, endpoints, URLs, etc.

**NOTE:** as of ``v0.3.0``, there are two different base API URLs:

1. "web": ``https://{code}.api.riotgames.com/``
2. "client": ``https://pd.{code}.a.pvp.net/``

You can choose between thse URLs with the optional ``base`` keyword
argument in both of the build functions:

.. code:: python

   h = client.build_header({"Authorization": f"Bearer {KEY}"}, base="client")
   url = client.build_url(code="na", endpoint="mmr", base="client")

.. _``.values``: https://github.com/IreTheKID/valorant.py/blob/master/valorant/values.py