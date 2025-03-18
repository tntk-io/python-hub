import requests

BASE_URL = 'https://jsonmock.hackerrank.com/api/weather/search'


def weatherStation(keyword, max_temp=None):
    records = []
    params = {
        'name': keyword,
        'page': 1
    }
    total_pages = 1

    while params['page'] <= total_pages:
        data = requests.get(BASE_URL, params=params).json()
        total_pages = data['total_pages']
        params['page'] += 1
        records.extend(data['data'])

    # Filter if max_temp specified
    if max_temp:
        records = [r for r in records if int(r['weather'].split()[0]) <= max_temp]

    # # Optional, since it's already sorted
    # records.sort(key=lambda d: d['name'])

    formatted = []
    for r in records:
        temperature = r['weather'].split()[0]
        wind = r['status'][0].split()[1][:-4]
        humidity = r['status'][1].split()[1][:-1]
        formatted.append(f'{r['name']},{temperature},{wind},{humidity}')

    # Return formatted strings
    return formatted


print(weatherStation('X', 16))
