import requests
import random
import webbrowser
import time

lastRequest = 0

servers_data = ""

def joinRandomServer(place_id):
    global lastRequest
    global servers_data

    join = False

    if time.time() - lastRequest >= 30:
        # URL for Roblox game instances (servers)
        api_url = f'https://games.roblox.com/v1/games/{place_id}/servers/Public?sortOrder=Asc&limit=100'

        # Fetch the list of active servers
        response = requests.get(api_url)
        newServers_data = response.json()

        if 'data' in newServers_data and len(newServers_data['data']) > 0:
            servers_data = newServers_data

    if 'data' in servers_data and len(servers_data['data']) > 0:
        join = True

    else:
        joinRandomServer(place_id)

    if join:
        servers = servers_data['data']

        # Choose a random server
        random_server = random.choice(servers)
        server_id = random_server['id']

        # Generate the Roblox server join link
        join_url = f'roblox://placeID={place_id}&gameInstanceId={server_id}'

        # Open the Roblox client to join the server
        webbrowser.open(join_url)

        return join_url