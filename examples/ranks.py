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
