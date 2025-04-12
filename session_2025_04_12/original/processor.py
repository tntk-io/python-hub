import json
from collections import defaultdict

import requests

with open('data.json') as file:
    releases = json.load(file)

most_wanted = max(releases, key=lambda r: r['stats']['community']['in_wantlist'])
print(f'The most wanted release is: {most_wanted['title']} by {most_wanted['artist']}')

most_collected = max(releases, key=lambda r: r['stats']['community']['in_wantlist'])
print(f'The most collected release is: {most_wanted['title']} by {most_wanted['artist']} with the following songs:')
release_info = requests.get(most_collected['resource_url']).json()
tracks = release_info['tracklist']
print('\n'.join(t['title'] for t in tracks))

release_per_year = defaultdict(int)

for release in releases:
    if 'year' in release:
        release_per_year[release['year']] += 1

for year, total in release_per_year.items():
    print(f'{year}: {total}')

total_main_role = sum(1 for r in releases if r['role'] == 'Main')

print(f'The artist has a main role in {total_main_role / len(releases) * 100:.2f}% of the releases.')

latest_master = min((r for r in releases if 'year' in r and r['type'] == 'master'), key=lambda r: r['year'])
print('Oldest videos:')
latest_data = requests.get(latest_master['resource_url']).json()
print('\n'.join(f'{v['title']}: {v['uri']}' for v in latest_data.get('videos', [])))

print('Downloading latest album cover')
latest_release = max((r for r in releases if 'year' in r and r['type'] == 'release'),
                     key=lambda r: r['year'])
print(latest_release)
images = requests.get(latest_release['resource_url']).json()['images']

user_agent_header = {
    'User-Agent': 'Your User Agent 1.0'
}

for index, image in enumerate(images, 1):
    print(f'{index}/{len(images)}')
    # print(image['resource_url'])
    with open(f'{latest_release['title']}-{latest_release['year']}-{index}.jpg'.replace('&', ''), 'wb') as file:
        file.write(requests.get(image['resource_url'], headers=user_agent_header).content)
