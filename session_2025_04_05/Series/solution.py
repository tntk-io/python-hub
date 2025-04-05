import datetime as dt
from collections import defaultdict

DATE_FORMAT = '%Y.%m.%d'


def day_of_the_week(year, month, day):
    days = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
    months = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if month < 3:
        year -= 1
    return days[(year + year // 4 - year // 100 + year // 400 + months[month - 1] + day) % 7]


class Episode:
    def __init__(self, date, title, ep_season, length, watched):
        self.date = None if date == 'NI' else dt.datetime.strptime(date, DATE_FORMAT)
        self.series_title = title
        self.season, self.episode = map(int, ep_season.split('x'))
        self.length = int(length)
        self.watched = watched == '1'

    @property
    def season_ep(self):
        return f'{self.season}x{str(self.episode).zfill(2)}'

    @property
    def day_of_the_week(self):
        if not self.date:
            return None
        return day_of_the_week(self.date.year, self.date.month, self.date.day)


episodes = []

with open('list.txt') as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 5):
        episodes.append(Episode(*lines[i:i + 5]))

known_episodes = sum(1 for ep in episodes if ep.date)
print(f'The list contains {known_episodes} episodes with known broadcasting date.')

total_episodes = len(episodes)
watched_episodes = sum(1 for ep in episodes if ep.watched)
print(f'The fan has watched {watched_episodes / total_episodes * 100:.2f}% of the episodes in the list.')

total_time_watched = sum(ep.length for ep in episodes if ep.watched)
# days = total_time_watched // (60 * 24)
# total_time_watched %= (60 * 24)
# hours = total_time_watched // 60
# minutes = total_time_watched % 60
time_watched = dt.datetime(1, 1, 1) + dt.timedelta(minutes=total_time_watched)

print(f'The fan spent {time_watched.day - 1} days {time_watched.hour} '
      f'hours and {time_watched.minute} minutes watching series.')

user_date = input('Enter a date. Date=\n')
user_date = dt.datetime.strptime(user_date, DATE_FORMAT)

episodes_not_watched = [ep for ep in episodes if ep.date and ep.date <= user_date and not ep.watched]

for ep in episodes_not_watched:
    print(f'{ep.season_ep}\t{ep.series_title}')

day = input('Enter a day of the week (e.g. Thu)! Day=\n')
series_on_day = {ep.series_title for ep in episodes if ep.day_of_the_week and ep.day_of_the_week == day}
print('\n'.join(series_on_day) if series_on_day else 'No series was broadcast on the given day.')

series = defaultdict(list)

for ep in episodes:
    series[ep.series_title].append(ep)

with open('sum.txt', 'w') as file:
    for series_title, episodes in series.items():
        file.write(f'{series_title} {sum(ep.length for ep in episodes)} {len(episodes)}\n')
