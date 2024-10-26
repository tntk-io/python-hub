import json
from random import choice

from game import Game
import logging
import os
import datetime as dt

if not os.path.exists('logs'):
    os.mkdir('logs')

NOW = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

logging.basicConfig(filename=f'logs/{NOW}.log', filemode='w', encoding='utf-8', datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(module)s - %(message)s')

if __name__ == '__main__':
    g = Game()
    g.start()
