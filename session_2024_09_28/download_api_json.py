import requests
import json

BASE_URL = 'https://jsonmock.hackerrank.com/api/weather/search'
total_pages = requests.get(BASE_URL).json()['total_pages']

records = []

for page in range(1, total_pages + 1):
    params = {
        'page': page
    }
    data = requests.get(BASE_URL, params=params).json()['data']
    records.extend(data)
    percentage = page / total_pages * 100
    print(f'{percentage:6.2f}% - {total_pages}/{str(page).zfill(2)}')

with open('hackerrank_weather.json', 'w', encoding='utf-8') as file:
    json.dump(records, file, indent=4, ensure_ascii=False)
