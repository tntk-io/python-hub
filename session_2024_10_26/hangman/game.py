import json
from random import choice
import os

import requests


def clear():
    return os.system('cls')


class Game:
    @staticmethod
    def load_steps(path='steps.json'):
        with open(path, encoding='utf-8') as file:
            steps = json.load(file)
            return ['\n'.join(step) for step in steps]

    @staticmethod
    def load_words(source='https://raw.githubusercontent.com/bevacqua/correcthorse/refs/heads/master/wordlist.json',
                   min_word_length=4):
        return [word for word in requests.get(source).json() if len(word) >= min_word_length]

    def __init__(self):
        self.steps = Game.load_steps()
        self.words = Game.load_words()

    def start(self):
        selected_word = choice(self.words).upper()
        print(selected_word)
        correct_guesses = []
        incorrect_guesses = []

        while set(correct_guesses) != set(selected_word) and len(incorrect_guesses) < len(self.steps) - 1:
            clear()
            print(self.steps[len(incorrect_guesses)])
            print(' '.join(c if c in correct_guesses else '_' for c in selected_word))
            print('Incorrect: ', ', '.join(incorrect_guesses))
            while True:
                guess = input('Enter a letter: ').upper()
                if guess in incorrect_guesses or guess in correct_guesses:
                    print(f'The letter "{guess}" has already been guessed.')
                    continue
                elif not ('A' <= guess <= 'Z') or len(guess) > 1:
                    print(f'"{guess}" is not a letter')
                    continue
                else:
                    break

            if guess in selected_word:
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)

        if len(incorrect_guesses) == len(self.steps) - 1:
            print(self.steps[len(incorrect_guesses)])
            print('Gamer over!')
        else:
            print('Victory!')
