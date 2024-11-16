import csv
from collections import Counter

data = []

with open('coffee.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line in reader:
        data.append(line)

print('The most common country was', Counter(d['Location.Country'] for d in data).most_common()[0][0])
print('The most common color of coffee beans was', Counter(d['Data.Color'] for d in data).most_common()[0][0])
highest_country = max(data, key=lambda d: int(d['Location.Altitude.Average']))
print('The highest country based on average altitude was', highest_country['Location.Country'])
