from flask import Flask, request, jsonify
from weather import WeatherRecord, WeatherResponse
import re
import math

app = Flask(__name__)

records = WeatherRecord.load_from_file()


@app.get('/search')
def search():
    name, page = request.args.get('name', default=''), request.args.get('page', default='1')

    if not page.isdigit() or int(page) == 0:
        return jsonify({'error': 'Invalid page number'})
    else:
        page = int(page)

    return jsonify(WeatherResponse(page, 10, name, records).to_dict())


if __name__ == '__main__':
    app.json.ensure_ascii = False
    app.json.sort_keys = False
    app.run(debug=True)
