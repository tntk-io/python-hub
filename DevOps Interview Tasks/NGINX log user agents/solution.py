import re
from collections import Counter

user_agent_pattern = re.compile(r'"(?P<user_agent>[^"]+)" "[^"]+"$')
user_agent_freq = Counter()

with open('access.log') as file:
    for line in file:
        m = user_agent_pattern.search(line)
        if m and m.group('user_agent') != '-':
            user_agent_freq[m.group('user_agent')] += 1
    ## Alternative without RegEx:
    # for line in file:
    #     user_agent = line.split('" "')[-2].split('"')[-1]
    #     if user_agent != "-":
    #         user_agent_freq[user_agent] += 1

for agent, freq in user_agent_freq.most_common(10):
    print(f'{agent}: {freq}')
