import boto3
import logging
import datetime as dt
import time


def milliseconds_since_epoch():
    return round(time.time() * 1000)


NOW = dt.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

client = boto3.client('logs')


class CloudWatchHandler(logging.Handler):
    def __init__(self, log_group_name='/hangman', log_stream_name=f'{NOW}.log'):
        super().__init__()
        # Log group must be created in advance
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name
        client.create_log_stream(logGroupName=self.log_group_name, logStreamName=self.log_stream_name)

    def emit(self, record: logging.LogRecord):
        events = [{
            'timestamp': milliseconds_since_epoch(),
            'message': self.format(record)
        }]
        client.put_log_events(logGroupName=self.log_group_name, logStreamName=self.log_stream_name, logEvents=events)


if __name__ == '__main__':
    logging.basicConfig(handlers={CloudWatchHandler()}, format='%(levelname)s:%(module)s - %(message)s')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.info('HELLO')
