import json
import math
import re


class WeatherRecord:
    weather_pattern = re.compile(r'(-?\d+)')
    wind_pattern = re.compile(r'Wind: (\d+)')
    humidity_pattern = re.compile(r'Humidity: (\d+)')

    @staticmethod
    def load_from_file(path='hackerrank_weather.json'):
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            records = []

            for record in data:
                records.append(WeatherRecord(record['name'], record['weather'], record['status']))
            return records

    @staticmethod
    def filter_data(data, name, min_temp, max_temp):
        filtered = []
        for r in data:
            if re.search(re.escape(name), r.name, flags=re.IGNORECASE) and \
                    (min_temp is None or r.weather >= min_temp) and (max_temp is None or r.weather <= max_temp):
                filtered.append(r)
        return filtered

    def __init__(self, name, weather, status):
        self.name = name
        self.weather = int(WeatherRecord.weather_pattern.match(weather).groups()[0])
        self.wind = int(WeatherRecord.wind_pattern.match(status[0]).groups()[0])
        self.humidity = int(WeatherRecord.humidity_pattern.match(status[1]).groups()[0])

    def to_dict(self):
        return {
            'name': self.name,
            'weather': f'{self.weather} degree',
            'status': [
                f'Wind: {self.wind}Kmph',
                f'Humidity: {self.humidity}%'
            ]
        }


class WeatherResponse:
    def __init__(self, page: int, per_page: int, name: str, data: [WeatherRecord], **kwargs):
        self.page = page
        self.per_page = per_page
        self.data = WeatherRecord.filter_data(data, name, kwargs.get('min_temp'), kwargs.get('max_temp'))
        self.total = len(self.data)
        self.total_pages = math.ceil(self.total / self.per_page)

    def select_page(self, page: int) -> [WeatherRecord]:
        return self.data[(page - 1) * self.per_page:page * self.per_page]

    def to_dict(self):
        return {
            'page': self.page,
            'per_page': self.per_page,
            'total': self.total,
            'total_pages': self.total_pages,
            'data': [r.to_dict() for r in self.select_page(self.page)]
        }
