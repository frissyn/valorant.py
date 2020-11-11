import os
import json
import valorant

KEY = os.environ["KEY"]

game = valorant.Client(KEY)

print(json.dumps(game.maps, indent=2))
