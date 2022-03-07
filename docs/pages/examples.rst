================
Library Examples
================

The following examples explore different features of the library and how to use them. These snippets should get you started with the basics by showing you how to use each feature in a practical manner.

Quickstart
~~~~~~~~~~

.. code-block:: python

    import valorant
    
    KEY = "RGAPI-Key-Here"
    client = valorant.Client(KEY)
    
    agents = client.get_characters()
    
    print(agents.get("Viper"))


Leaderboard
~~~~~~~~~~~

.. code-block:: python

    # Get the ranked leaderboard of a region and print the 
    # top players. Shows leaderboard rank, game name, and
    # number of wins. See documentation on `Client.get_leaderboard`
    # for more info.
    
    import os
    import valorant
    
    KEY = os.environ["VALPY-KEY"]
    
    # Set our client's region to EU. Client uses NA by default.
    client = valorant.Client(KEY, region="eu")
    
    # Get the top 15 players on the Ranked Leaderboard.
    lb = client.get_leaderboard(size=15)
    
    print("Top Players in EU:\n")
    
    # Print all players on the leaderboard.
    for p in lb.players:
        print(f"#{p.leaderboardRank} - {p.gameName} ({p.numberOfWins} wins)")


Queries
~~~~~~~

See the :doc:`guides/queries` page for more details.

.. code-block:: python

    # valorant.py provides some powerful helper functions
    # for filtering data from the API. These snippets cover
    # both simple and advanced use cases.
    
    import os
    import valorant
    
    from valorant.query import exp
    
    KEY = os.environ["VALPY-KEY"]
    client = valorant.Client(KEY, locale=None)
    
    # Find the Phantom among the list of weapons.
    # `.find` is an alias for `.get`, provided for semantics.
    weapon = client.get_equips().get(name="Phantom")
    
    # Using `.get` without a keyword defaults to using 'name'.
    agent = client.get_characters().get("Viper")
    
    lb = client.get_leaderboard(size=100)
    
    # Find all the players on the leaderboard with 10 wins.
    # `.find_all` is an alias for `.get_all`, provided for semantics.
    players = lb.players.get_all(numberOfWins=10)
    
    
    # You can generate an expression to make more detailed queries.
    # valorant.py expressions support both object and logical comparisons,
    # as well as using member functions that return booleans or boolean-like
    # objects. `valorant.query.exp` is factory method used to build 
    # these expressions.
    
    # Find all the players on the leaderboard with more than 10 wins.
    players = lb.players.get_all(numberOfWins=exp('>=', 10))
    
    # Only get players from the XSET org on the leaderboard.
    players = lb.players.get_all(gameName=exp('.startswith', 'XSET'))
    
    # You can also pass callables that take the attribute value as
    # a prameter and return a boolean or boolean-like object.
    
    # This line is functionally the same as the above.
    players = lb.players.get_all(gameName=lambda a: a.startswith('XSET'))


Ranks
~~~~~

.. code-block:: python

    # Get the most recent Ranked match in a user's history,
    # and print the ranks of every player in the match. If
    # there isn't a Ranked match in the history, the program
    # will exit. **This example requires an API Key with access
    # to the match endpoint. You need to apply for that from
    # the Riot Games Developer Portal.**
    
    import os
    import valorant
    
    KEY = os.environ["VALPY-KEY"]
    client = valorant.Client(KEY, locale="en-US")
    
    # Get a user by name and tagline.
    account = client.get_user_by_name("frissyn#6969")
    
    # Find their most recent Ranked match.
    # This will raise an error if your API Key does not have match access.
    match = account.matchlist().history.find(queueId="competitive")
    
    # Check if the match exists.
    if match == None:
        print("No Ranked match in recent history!")
        exit(1)
    else:
        match = match.get()
    
    # Print everyone's ranks.
    for team in match.teams:
        print(f"{team.teamId} Team's Ranks: ")
    
        # Find all the players on the same team.
        players = match.players.get_all(teamId=team.teamId)
    
        for player in players:
            print(f"\t{player.gameName} - {player.rank}")
