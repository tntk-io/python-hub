import json
from collections import defaultdict
from time import sleep

import requests

with open('data.json', encoding='utf-8') as file:
    releases = json.load(file)

# All maximum in_wantlist releases
max_in_wantlist = max(r['stats']['community']['in_wantlist'] for r in releases)
print(max_in_wantlist)
max_in_wantlist_release = next((r for r in releases if r['stats']['community']['in_wantlist'] == max_in_wantlist),
                               'N/A')
print(f'{max_in_wantlist_release['title']} - {max_in_wantlist_release['artist']}')

# # One of the maximum in_wantlist releases
# def get_in_wantlist(r):
#     return r['stats']['community']['in_wantlist']


max_in_wantlist_release = max(releases, key=lambda r: r['stats']['community']['in_wantlist'])
print(f'{max_in_wantlist_release['title']} - {max_in_wantlist_release['artist']}')

# Most Collected Songs

max_collected_release = max(releases, key=lambda r: r['stats']['community']['in_collection'])
print(f'{max_collected_release['title']} - {max_collected_release['artist']}')

release_info = requests.get(max_collected_release['resource_url']).json()
tracks = release_info['tracklist']
print('\n'.join(t['title'] for t in tracks))

year_releases = defaultdict(int)
for r in releases:
    if 'year' in r:
        year_releases[r['year']] += 1

for year, total in year_releases.items():
    print(f'{year}: {total}')

number_of_main_roles = sum(1 for r in releases if r['role'] == 'Main')
print(f'The artist had a main role in {number_of_main_roles / len(releases) * 100:.2f}% of the releases')

print('Oldest videos:')
oldest_release = next(r for r in releases if r['type'] == 'master' and 'year' in r)
oldest_release_info = requests.get(oldest_release['resource_url']).json()
videos = oldest_release_info.get('videos', [])

for v in videos:
    print(f'{v['title']}: {v['uri']}')

print('Downloading cover(s) of the latest release:')
latest_release = next(r for r in reversed(releases) if r['type'] == 'release' and 'year' in r)
latest_release_info = requests.get(latest_release['resource_url']).json()
images = latest_release_info['images']

headers = {
    'User-Agent': 'Tentek 1.0'
}

for counter, image in enumerate(images, 1):
    print(f'{counter}/{len(images)}')
    with open(f'{latest_release['title']}-{latest_release['year']}-{counter}.jpg', 'wb') as file:
        response = requests.get(image['resource_url'], headers=headers)
        file.write(response.content)
    if counter < len(images):
        sleep(1)
