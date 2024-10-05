import os
from collections import Counter
from random import randint

import pytest


def count(s):
    d = {}

    # # Failure imitation
    # if len([c for c in s if 0 <= c <= 1000]) > 0:
    #     return {}

    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def generate_sequences():
    for i in range(100):
        l = []
        for j in range(randint(10, 50)):
            l.append(randint(-5000, 5000))
        yield l, Counter(l)


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
            generate_sequences()
    )
)
def test_common_elements(s, expected):
    assert count(s) == expected


@pytest.fixture(autouse=True, scope='function')
def tempfile():
    with open('test.log', 'w') as file:
        file.write('EXAMPLE')
    yield
    os.remove('test.log')


def test_log():
    with open('test.log', 'r+') as file:
        assert file.read() == 'EXAMPLE'
        file.write('test')


def test_log2():
    with open('test.log') as file:
        assert file.read() == 'EXAMPLE'
