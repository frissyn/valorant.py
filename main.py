import os
import json
import valorant

API_KEY = os.getenv("API_KEY")
client = valorant.Client(API_KEY)

agents = client.get_characters()

for agent in agents:
	print(json.dumps(agent.json, indent=2))
