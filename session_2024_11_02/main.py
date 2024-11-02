import re

import requests
import xml.etree.ElementTree as ET
from jinja2 import Template


class Item:
    def __init__(self, title, description, link, thumbnail=''):
        self.title = title
        self.description = description
        self.link = link
        self.thumbnail = thumbnail

    @staticmethod
    def from_element(element, namespaces):
        return Item(element.find('title').text, element.find('description').text, element.find('link').text,
                    element.find('media:thumbnail', namespaces=namespaces).attrib['url'])


BBC_URL = 'https://feeds.bbci.co.uk/news/world/rss.xml'
response = requests.get(BBC_URL)

text = response.text
first_line = text.split('\n')[0]
namespaces = {t[0]: t[1] for t in re.findall(r'xmlns:(?P<namespace>.*?)=\"(?P<url>.*?)\"', first_line)}

root = ET.fromstring(response.text)
channel = root.find('channel')

items = [Item.from_element(element, namespaces) for element in channel.findall('item')]

with open('templates/bulletin.html') as file:
    template = Template(file.read())

rendered = template.render(items=items)

with open('output.html', 'w', encoding='utf-8') as file:
    file.write(rendered)
