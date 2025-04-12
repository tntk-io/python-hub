import json

import requests
from time import sleep

artist_id = 124535
data = requests.get(f'https://api.discogs.com/artists/{artist_id}/releases').json()

url = f'https://api.discogs.com/artists/{artist_id}/releases'
releases = []

params = {
    'per_page': 500
}

while url:
    data = requests.get(url, params=params).json()
    print(f"Current page: {data['pagination']['page']}/{data['pagination']['pages']}")
    releases.extend(data['releases'])
    url = data['pagination']['urls'].get('next')
    if url:
        sleep(1)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(releases, file, indent=4)
