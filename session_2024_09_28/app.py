from flask import Flask, request, jsonify
from session_2024_09_28.weather import WeatherRecord, WeatherResponse

app = Flask(__name__)

records = WeatherRecord.load_from_file()


def error(message):
    return jsonify({
        'error': message
    })


@app.get('/search')
def search():
    name = request.args.get('name', default='')
    page = request.args.get('page', default='1')
    per_page = request.args.get('per_page', default='10')
    min_temp = request.args.get('min_temp')
    max_temp = request.args.get('max_temp')

    if not page.isdigit() or int(page) == 0:
        return error('Invalid page number')
    else:
        page = int(page)

    if not per_page.isdigit() or int(per_page) < 1:
        return jsonify({'error': 'Invalid number per page'})
    else:
        per_page = int(per_page)

    if min_temp is not None:
        min_temp_match = WeatherRecord.weather_pattern.fullmatch(min_temp)
        if min_temp_match is None:
            return error('Invalid min_temp')
        else:
            min_temp = int(min_temp_match.group())
    if max_temp is not None:
        max_temp_match = WeatherRecord.weather_pattern.fullmatch(max_temp)
        if max_temp_match is None:
            return error('Invalid max_temp')
        else:
            max_temp = int(max_temp_match.group())

    if (max_temp is not None and min_temp is not None) and max_temp < min_temp:
        return error('Invalid temperatures, min_temp cannot be greater than max_temp')

    return jsonify(WeatherResponse(page, per_page, name, records, min_temp=min_temp, max_temp=max_temp).to_dict())


if __name__ == '__main__':
    app.json.ensure_ascii = False
    app.json.sort_keys = False
    app.run(debug=True)
