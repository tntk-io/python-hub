import json
import logging
from random import choice

from clear import clear
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Game:
    @staticmethod
    def load_steps(path='steps.json'):
        logger.info('Loading steps.')
        with open(path, encoding='utf-8') as file:
            steps = json.load(file)
            return ['\n'.join(step) for step in steps]

    @staticmethod
    def load_words(source='https://raw.githubusercontent.com/bevacqua/correcthorse/refs/heads/master/wordlist.json',
                   min_word_length=4):
        logger.info('Loading words.')
        return [word for word in requests.get(source).json() if len(word) >= min_word_length]

    def __init__(self):
        self.steps = Game.load_steps()
        self.words = Game.load_words()
        logger.debug(f'{len(self.steps)} steps, {len(self.words)} words loaded.')

    def start(self):
        logger.info('Game started.')
        selected_word = choice(self.words).upper()
        logger.debug(f'The selected word was: {selected_word}')
        correct_guesses = []
        incorrect_guesses = []

        while set(correct_guesses) != set(selected_word) and len(incorrect_guesses) < len(self.steps) - 1:
            clear()
            print(self.steps[len(incorrect_guesses)])
            print(' '.join(c if c in correct_guesses else '_' for c in selected_word))
            print('Incorrect: ', ', '.join(incorrect_guesses))
            while True:
                logger.info('Prompting the user.')
                guess = input('Enter a letter: ').upper()
                logger.debug(f'User entered: "{guess}"')
                if guess in incorrect_guesses or guess in correct_guesses:
                    print(f'The letter "{guess}" has already been guessed.')
                    logger.error('Already existing guess entered.')
                    continue
                elif not ('A' <= guess <= 'Z') or len(guess) > 1:
                    print(f'"{guess}" is not a letter')
                    logger.error('Non-letter character entered.')
                    continue
                else:
                    break

            if guess in selected_word:
                correct_guesses.append(guess)
                logger.info('Correct guess.')
            else:
                incorrect_guesses.append(guess)
                logger.info('Incorrect guess.')

        if len(incorrect_guesses) == len(self.steps) - 1:
            print(self.steps[len(incorrect_guesses)])
            print('Gamer over!')
            logger.info('Defeat.')
            return False, len(incorrect_guesses)
        else:
            logger.info('Victory.')
            print('Victory!')
            return True, len(incorrect_guesses)
