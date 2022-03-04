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

print(players)