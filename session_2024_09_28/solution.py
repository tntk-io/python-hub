import requests
from weather import WeatherRecord

BASE_URL = 'https://jsonmock.hackerrank.com/api/weather/search'


def weatherStation(keyword, max_temp=None):
    params = {
        'name': keyword,
        'page': 1
    }
    total_pages = None

    records: [WeatherRecord] = []

    while not total_pages or params['page'] <= total_pages:
        data = requests.get(BASE_URL, params=params).json()
        total_pages = data['total_pages']
        for record in data['data']:
            parsed_record = WeatherRecord(record['name'], record['weather'], record['status'])
            if max_temp is None or parsed_record.weather <= max_temp:
                records.append(parsed_record)
        params['page'] += 1

    print([r.to_dict() for r in records])


weatherStation('ar', max_temp=10)
