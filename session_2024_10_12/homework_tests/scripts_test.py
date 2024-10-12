from random import randint
import pytest
from time import sleep

from scripts import reverse_list, current_time
import datetime as dt


@pytest.mark.parametrize(
    'l',
    (
            [1, 2, 3],
            [],
            list(range(100000)),
            [1, 'a', 1.2, True],
            [[], [True], [True, False], 'oio'],
            [{'test': 11, 12: 'test'}, 1.2],
    )
)
def test_reverse_list(l):
    assert l[::-1] == reverse_list(l)


def test_current_time():
    for i in range(10):
        now_remote = current_time()
        now_local = dt.datetime.now(dt.timezone.utc)
        diff = now_local - now_remote
        assert diff.seconds <= 2
        sleep(randint(1, 3))
