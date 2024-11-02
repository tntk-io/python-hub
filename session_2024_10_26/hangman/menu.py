import json
from random import choice

from clear import clear
from game import Game
import logging
import os
import datetime as dt
from aws_logger import CloudWatchHandler

if not os.path.exists('logs'):
    os.mkdir('logs')

NOW = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

logging.basicConfig(filename=f'logs/{NOW}.log', filemode='w', encoding='utf-8', datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(module)s - %(message)s')


# logging.basicConfig(handlers={CloudWatchHandler()}, format='%(levelname)s:%(module)s - %(message)s')


# UserInfo -> username, victories, total_games, incorrect_guesses
class UserInfo:
    def __init__(self, username, victories, total_games, incorrect_guesses):
        self.username = username
        self.victories = victories
        self.total_games = total_games
        self.incorrect_guesses = incorrect_guesses

    @property
    def victory_percentage(self):
        return self.victories / self.total_games * 100

    @property
    def average_incorrect_guesses(self):
        return self.incorrect_guesses / self.total_games

    @staticmethod
    def from_dict(d):
        return UserInfo(d['username'], d['victories'], d['total_games'], d['incorrect_guesses'])

    def to_dict(self):
        return {
            'username': self.username,
            'victories': self.victories,
            'total_games': self.total_games,
            'incorrect_guesses': self.incorrect_guesses
        }

    def __str__(self):
        return f'{self.username} ({self.victory_percentage:.0f}% victory) - {self.average_incorrect_guesses:.2f}'


# Leaderboard
# Stores list of UserInfo
class Leaderboard:
    users = {}

    def __init__(self, path='leaderboard.json'):
        self.path = path
        self.load()

    def add_info(self, info: UserInfo):
        if info.username in self.users:
            selected_user = self.users[info.username]
            selected_user.victories += info.victories
            selected_user.total_games += info.total_games
            selected_user.incorrect_guesses += info.incorrect_guesses
        else:
            self.users[info.username] = info

    def load(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                json.dump({}, file)

        with open(self.path, encoding='utf-8') as file:
            d = json.load(file)
            for k, v in d.items():
                self.users[k] = UserInfo.from_dict(v)

    def save(self):
        with open(self.path, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def to_dict(self):
        return {
            username: user_info.to_dict() for username, user_info in self.users.items()
        }

    def __str__(self):
        sorted_users = sorted(self.users.values(), key=lambda u: u.victory_percentage, reverse=True)
        return '\n'.join([str(u) for u in sorted_users])


if __name__ == '__main__':
    leaderboard = Leaderboard()
    while True:
        clear()
        print('1. New Game')
        print('2. Leaderboard')
        print('3. Exit')
        option = input('')

        match option:
            case '1':
                g = Game()
                victory, incorrect_guesses = g.start()
                username = input('Enter your username: ')
                info = UserInfo(username, int(victory), 1, incorrect_guesses)
                leaderboard.add_info(info)
                leaderboard.save()
            case '2':
                print(str(leaderboard))
                input()
            case '3':
                exit(0)
