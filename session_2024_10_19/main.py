import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s]:%(name)s: %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S%z')

logger = logging.getLogger(__name__)
logging.debug('will this appear')
logging.info('TEST')

logging.root.handlers[0].formatter = logging.Formatter('CHANGED: %(asctime)s [%(levelname)s]: %(message)s')
handler = logging.FileHandler('main.log')
handler.formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
# logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.debug('example1')
logger.info('example2')

# try:
#     1 / 0
# except ZeroDivisionError:
#     logging.exception('This user once again divided by zero')
#
# number = input('Enter a positive number: ')
# if not number.isdigit():
#     logging.error('User entered text when number was expected')
# else:
#     number = int(number)
#     print(f'{number} + 5 = {number + 5}')
