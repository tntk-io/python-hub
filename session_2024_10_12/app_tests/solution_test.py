import pytest

from session_2024_09_28.solution import Solution


@pytest.fixture(scope='session')
def remote_solution():
    return Solution('https://jsonmock.hackerrank.com/api/weather/search')


@pytest.fixture(scope='session')
def local_solution():
    return Solution('http://127.0.0.1:5000/search')


@pytest.mark.parametrize(
    ('keyword', 'max_temp'),
    (
            # ('', None),
            ('ab', None),
            ('afdsoijaoif', None),
            ('', -20),
            ('\\', None),
            ('*', None),
            ('.', None),
            ('ba', None),
            ('a', 0),
            ('a', 10),
            ('a', -10),
    )
)
def test_solution(remote_solution, local_solution, keyword, max_temp):
    assert local_solution.weatherStation(keyword, max_temp) == remote_solution.weatherStation(keyword, max_temp)
