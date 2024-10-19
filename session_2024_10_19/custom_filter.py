import logging
from collections import defaultdict


class CustomFilter(logging.Filter):
    # Keyword and level
    conditions = defaultdict(list)

    def add_condition(self, level, keyword):
        self.conditions[level].append(keyword)

    def __init__(self, name):
        super().__init__(name)

    def filter(self, record: logging.LogRecord) -> bool:
        for keyword in self.conditions[record.levelname]:
            if keyword.lower() in record.getMessage().lower():
                return False
        return True


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
custom_filter = CustomFilter('My custom filter')
custom_filter.add_condition('INFO', 'something')
custom_filter.add_condition('ERROR', 'notsocritical')
logger.addFilter(custom_filter)

logger.info('Added something')
logger.info('Only this should appear')
logger.error('Added something')
logger.error('notsocritical: something not so important happened')
logging.info('Added something')
logging.info('Added something')
