================================
Introduction to the Valorant API
================================

.. currentmodule:: valorant

Assuming you've read the :doc:`installing` guide, you're almost ready to start interacting with the Valorant API. But first, you need an API Key.

Getting an API Key
~~~~~~~~~~~~~~~~~~

1. If you haven't already, head over to the `Riot Games Developer Portal <https://developer.riotgames.com/>`_ and log in or create an account.

2. Go back to the home page, scroll down a bit and look for the **Developement API Key** section. It should look like this:

    .. image:: ../../images/dev-api-portal.jpg
        :width: 60%
        :alt: Riot Games Developer API Portal

3. Generate a new API key, and copy it into your project enviornment. (Enviornment variable, ``.env`` file, etc.)

4. That's it! You're ready to access the API using ``valorant.py`` now.

Making Requests
~~~~~~~~~~~~~~~

Now let's get started using the library. Here's some sample code:

.. code-block:: python
    :linenos:

    import os
    import valorant
    
    KEY = os.environ["VALPY-KEY"]
    client = valorant.Client(KEY, locale=None)
    
    skins = client.get_skins()
    name = input("Search a Valorant Skin Collection: ")
    
    results = skins.find_all(name=lambda x: name.lower() in x.lower())
    
    print("\nResults: ")
    for skin in results:
        print(f"\t{skin.name.ljust(21)} ({skin.localizedNames['ja-JP']})")


That's a lot to cover, so let's run through it step by step.

1. The ``import`` statements let us use the packages we need. ``os`` to access or API key from the enviornment, and ``valorant`` to interact with the API.

2. The 5th line creates an instance of the :class:`Client`, which represents our connection to the Valorant API. By setting ``locale`` to ``None`` we can get content data in other languages, which will be handy in a second.

3. 
