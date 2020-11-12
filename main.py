import os
import valorant

API_KEY = os.environ("API_KEY")
client = valorant.Client(API_KEY)

agents = client.get_characters()

for agent in agents:
    print(agent.name)
