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


if __name__ == '__main__':
    now_remote = current_time()
    now_local = dt.datetime.now(dt.timezone.utc)
    diff = now_local - now_remote
