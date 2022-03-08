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

Now let's get started using the library. Creating a new Python file, ``val_example.py``, let's put in some sample code:

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

3. Next we make a request to the API for data on Gun and Melee Skins. This is a :class:`ContentList` of :class:`ContentItemDTO` objects, each representing a Skin.

4. Now we want to get a skin collection name from the user, and show them all the gun skins in that collection. So the 8th line will get the user's input as ``name``.

5. The 10th line is the most important of all. Here we use the query function :func:`ContentList.get_all` in order to serch the list of skins. We want to match every skin that has the given collection in its name, so we use the expression ``name in x.name``. ``x`` is the skin object, and by passing that expression as a lambda into the attribute, that expression will be matched against every skin in the list.

6. Now that we have our list of skins in the ``results`` variable, let's print it out to the user! Lines 13 and 14 loop through the results and print each skin's name in a nice and neat manner :>

7. And as an added bonus, because we didn't give the client a locale, we can also display each skin's Japanese name as well, using ``skin.localizedNames['ja-JP']``.

Now to run it!

.. code-block:: shell

    $ python val_example.py

Assuming everything goes well, your program should run smoothly and look like this:

.. image:: ../../images/intro-result.jpg
    :width: 60%
    :alt: Example Program Result

Congrats, you've written your first program with ``valorant.py``! Check out the other guides for more.