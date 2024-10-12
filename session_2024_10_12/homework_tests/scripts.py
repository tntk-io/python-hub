from itertools import product

import requests
import datetime as dt


def reverse_list(l):
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l


def current_time():
    utc_datetime_text = requests.get('https://worldtimeapi.org/api/ip').json()['utc_datetime']
    utc_datetime = dt.datetime.fromisoformat(utc_datetime_text)
    return utc_datetime


def cartesian(l1, l2):
    res = []
    for a in l1:
        for b in l2:
            res.append((a, b))
    return res


if __name__ == '__main__':
    # now_remote = current_time()
    # now_local = dt.datetime.now(dt.timezone.utc)
    # diff = now_local - now_remote
    l1, l2 = list(range(1, 4)), list(range(6, 9))
    print(cartesian(l1, l2))
    print(list(product(l1, l2)))
