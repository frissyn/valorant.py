=============================
Using Expressions and Queries
=============================

.. currentmodule:: valorant

Simple Queries
~~~~~~~~~~~~~~

``valorant.py`` provides simple yet powerful utilites for filtering data from API responses.

For example, ``Client.get_characters`` returns a :class:`ContentList` of :class:`ContentItemDTO` objects that each represent a single Valorant agent.

.. code-block:: python

    import valorant

    client = valorant.Client("API-KEY")

    agents = client.get_characters()


The ContentList is a subclass of the built-in Python `list <https://docs.python.org/3/library/stdtypes.html#list>`_, but provides two filter utilities: ``get`` and ``get_all``. These functions search through the iterable for the first element that meets all the traits passed to them as keyword arguments. (Or a list of elements in `get_all`'s case.)

Say you wanted Viper's agent data:

.. code-block:: python

    viper = agents.get(name="Viper")

Or maybe the current act:

.. code-block:: python

    acts = client.get_acts()

    act = acts.get(isActive=True)

Expressions
~~~~~~~~~~~

``valorant.py`` also provides expression builders to create more complex queries. These utilities are most useful when filtering data from a more data intensive list, like the players on a :class:`LeaderboardDTO`. Let's assume the following leaderboard:

.. code-block:: python

    lb = client.get_leaderboard(size=100)

What if we wanted to get all the players on the leaderboard with more than 15 wins? The :func:`exp` function can be used to build an expression for that. Using this alongside the ``ContentList.get_all`` function will return all matching elements, instead of just the first one.


.. code-block:: python

    from valorant.query import exp

    players = lb.players.get_all(numberOfWins=exp('>=', 15))

The ``exp(`>=`, 15)`` function will generate a lambda that uses the ``>=`` operator to compare ``player.numberOfWins`` to our given value: ``15``. The above snippet is equivalent to:

.. code-block:: python

    players = []
    for player in lb.players:
        if player.numberOfWins >= 15:
            players.append(players)

:func:`exp` takes two arguments: the operator to compare with (``==``, ``in``, ``>=``, etc.) and the value to compare to. The value can be anything.

Expressions also support member functions, which use the dot (``.``) operator to access each element's function, assuming it returns a boolean or boolean-like object.

Let's say you wanted all the XSET players on the leaderboard. You'd need to check if the player's name start with the `XSET` prefix (assuming they haven't changed their in-game name). That looks like this:

.. code-block:: python

    players = lb.players.get_all(gameName=exp('.startswith', 'XSET'))


Custom Checks
~~~~~~~~~~~~~

Besides attribute values and expressions, you can also pass any callable that returns a boolean or boolean-like object to match for an element trait. These usually take the form of `lambdas`.

This example is equivalent to the previous snippet:

.. code-block:: python

    players = lb.players.get_all(gameName=lambda x: x.startswith('XSET'))

For more powerful queries, you could pass an entire function:

.. code-block:: python

    def name_check(attr: str):
        for prefix in ["SEN", "XSET", "100T", ...]:
            if attr.startswith(prefix):
                return True
    
        return False
    
    players = lb.players.get_all(gameName=name_check)
