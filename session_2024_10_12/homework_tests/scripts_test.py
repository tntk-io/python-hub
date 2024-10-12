from itertools import chain, product
from random import randint
import pytest
from time import sleep

from scripts import reverse_list, current_time, cartesian
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


def cartesian_edge_cases():
    l_t = [
        ([], []),
        ([True, 1.0, 'hi'], [False, -10]),
        ([[], {}, []], [(), [], {}]),
        ([None, 0], []),
        (['a', 'b'], [1, 2]),
        (['1', '2', '3'], ['x'])
    ]

    for l1, l2 in l_t:
        yield l1, l2, list(product(l1, l2))


def cartesian_random_cases():
    for _ in range(500):
        lists = []
        for _ in range(2):
            lists.append([randint(-5000, 5000) for _ in range(100, 400)])
        yield lists[0], lists[1], list(product(lists[0], lists[1]))


@pytest.mark.parametrize(
    ('l1', 'l2', 'expected'),
    (
            chain(cartesian_edge_cases(), cartesian_random_cases())
    )
)
def test_cartesian(l1, l2, expected):
    assert cartesian(l1, l2) == expected
