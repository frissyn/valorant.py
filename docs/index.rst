.. valorant documentation master file, created by
   sphinx-quickstart on Mon May 10 16:57:23 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

valorant.py
====================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   valorant
   requests
   endpoints


``valorant.py`` is an unofficial API wrapper for Riot Games' Valorant
API endpoints. It's modern, easy to use, feature-rich, and intuitive!
Implemented with object oriented designs and explicit reloads to prevent
``429``\ s, valorant.py is the best Valorant API wrapper out there!



Quickstart Examples:
--------------------

Client:

.. code:: py

   import valorant

   KEY = "RGAPI-Key-Here"
   client = valorant.Client(KEY)

   agents = client.get_characters()

   for agent in agents:
       print(agent.name)

Asynchronous Client:

.. code:: py

   import valorant

   KEY = "RGAPI-Key-Here"
   client = valorant.AsyncClient(KEY)

   async def _main():
       agents = await client.get_characters()

       for agent in agents:
           print(agent.name)

   valorant.run(_main())

Local Client:

*This is intended for use with the game locally. Eases the use of doing
things like getting live match data, chat sessions, friend requests,
etc. Doesn't need an access key.*

.. code:: python

   import valorant

   client = valorant.LocalClient()

   print(client.get_session())
