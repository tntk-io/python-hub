from collections import defaultdict
from datetime import datetime, timedelta


def day_of_the_week(year, month, day):
    dow = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    months = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if month < 3:
        year -= 1
    return dow[(year + year // 4 - year // 100 + year // 400 + months[month - 1] + day) % 7]


class Episode:
    def __init__(self, date, title, season_episode, length, watched):
        self.date = None if date == 'NI' else datetime.strptime(date, '%Y.%m.%d')
        self.title = title
        self.season, self.season_episode = map(int, season_episode.split('x'))
        self.length = int(length)
        self.watched = watched == '1'

    @property
    def day_of_the_week(self):
        return None if not self.date else day_of_the_week(self.date.year, self.date.month, self.date.day)


episodes = []

with open('list.txt') as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 5):
        episodes.append(Episode(*lines[i:i + 5]))

print('Exercise 2:')
print(f'The list contains {sum(1 for e in episodes if e.date)} episodes with known broadcasting date. ')

print('Exercise 3:')
print(
    f'The fan has watched {sum(1 for e in episodes if e.watched) / len(episodes) * 100:.2f}% of the episodes in the list.')

print('Exercise 4:')
total_minutes_watched = sum(e.length for e in episodes if e.watched)
td = timedelta(minutes=total_minutes_watched)
watch_time = datetime(1, 1, 1) + td
print(
    f'The fan spent {watch_time.day - 1} days {watch_time.hour} hours and {watch_time.minute} minutes watching series.')

print('Exercise 5:')
# date = datetime.strptime(input('Enter a date. Date='), '%Y.%m.%d')
date = datetime(2017, 10, 18)
not_watched_till_date = [e for e in episodes if not e.watched and e.date and e.date <= date]
for e in not_watched_till_date:
    print(f'{e.season}x{str(e.season_episode).zfill(2)}\t\t{e.title}')

print('Exercise 7:')
day = input('Enter a day of the week (e.g. Thu)! Day=')
episodes_on_day = [e for e in episodes if e.day_of_the_week == day]
print('No series was broadcasted on the given day.' if not episodes_on_day else '\n'.join(
    {e.title for e in episodes_on_day}))

series = defaultdict(list)

for e in episodes:
    series[e.title].append(e)

with open('sum.txt', 'w') as file:
    for s, eps in series.items():
        file.write(f'{s} {sum(e.length for e in eps)} {len(eps)}\n')
