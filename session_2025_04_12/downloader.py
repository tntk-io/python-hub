import json

import requests
from time import sleep

artist_id = 176766

params = {
    'per_page': 500
}
page = 1

url = f'https://api.discogs.com/artists/{artist_id}/releases'
releases = []

while url:
    page += 1
    data = requests.get(url, params=params).json()
    print(f'{data['pagination']['page']}/{data['pagination']['pages']}')
    releases.extend(data['releases'])
    url = data['pagination']['urls'].get('next')
    if url:
        sleep(1)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(releases, file, indent=4)
