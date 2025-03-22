from collections import defaultdict
from csv import DictReader


class Airport:
    def __init__(self, data):
        self.code = data['Airport.Code']
        self.name = data['Airport.Name']


class Statistics:
    def __init__(self, data):
        self.total_flights = int(data['Statistics.Flights.Total'])
        self.delayed_flights = int(data['Statistics.Flights.Delayed'])
        self.delayed_carrier = int(data['Statistics.# of Delays.Carrier'])
        self.delayed_late_aircraft = int(data['Statistics.# of Delays.Late Aircraft'])
        self.delayed_aviation_system = int(data['Statistics.# of Delays.National Aviation System'])
        self.delayed_security = int(data['Statistics.# of Delays.Security'])
        self.delayed_weather = int(data['Statistics.# of Delays.Weather'])
        self.on_time = int(data['Statistics.Flights.On Time'])
        self.canceled = int(data['Statistics.Flights.Cancelled'])
        self.delay_minutes_late_aircraft = int(data['Statistics.Minutes Delayed.Late Aircraft'])
        self.carriers = data['Statistics.Carriers.Names'].split(',')


class Time:
    def __init__(self, data):
        self.label = data['Time.Label']
        self.month = int(data['Time.Month'])
        self.year = int(data['Time.Year'])


class Record:
    def __init__(self, data):
        self.airport = Airport(data)
        self.statistics = Statistics(data)
        self.time = Time(data)


records = []

with open('airlines.csv') as file:
    # File is accessible here
    reader = DictReader(file)
    for d in reader:
        records.append(Record(d))
# File closed after exiting the block

# What is the total number of flights at Los Angeles (LAX) airport?
print(
    f'The total number of flights is: {sum(r.statistics.total_flights for r in records if r.airport.code == 'LAX'):,}')

# What is the average percentage of delayed flights?
total_flights = sum(r.statistics.total_flights for r in records)
delayed_flights = sum(r.statistics.delayed_flights for r in records)
print(f'There were a total of {total_flights:,} flights of which {delayed_flights:,} were delayed. '
      f'The ratio of delayed flights is: {delayed_flights / total_flights * 100:.2f}%')

# In total, what percentage of delays were due to security,
# weather, the national aviation system, late aircraft or delayed carriers?
delayed_security = sum(r.statistics.delayed_security for r in records)
delayed_weather = sum(r.statistics.delayed_weather for r in records)
delayed_aviation_system = sum(r.statistics.delayed_aviation_system for r in records)
delayed_late_aircraft = sum(r.statistics.delayed_late_aircraft for r in records)
delayed_carrier = sum(r.statistics.delayed_carrier for r in records)

print('Causes of delayed flights:')
print(f'National aviation system: {delayed_aviation_system / delayed_flights * 100:.2f}%')
print(f'Late aircraft: {delayed_late_aircraft / delayed_flights * 100:.2f}%')
print(f'Late carrier: {delayed_carrier / delayed_flights * 100:.2f}%')
print(f'Weather: {delayed_weather / delayed_flights * 100:.2f}%')
print(f'Security: {delayed_security / delayed_flights * 100:.2f}%')

# How many airports can be found in the dataset given that the airport codes are unique?
unique_airports = {r.airport.code for r in records}
print(f'The number of unique airports is: {len(unique_airports)}')

# What percentage of the flights were on time at LaGuardia Airport (LGA), NYC in the month of September, 2012?
# lga = None
#
# for r in records:
#     if r.airport.code == 'LGA' and r.time.year == 2012 and r.time.month == 9:
#         lga = r
#         break
#
# print(lga.airport.name, lga.time.label)

lga = next((r for r in records if r.time.year == 2012 and r.time.month == 9 and r.airport.code == 'LGA'),
           None)
print(
    f'{lga.statistics.on_time / lga.statistics.total_flights * 100:.2f}% of the flights were on time at LGA in September, 2012')

# How many years do the records span?
print(f'The records span over {max(r.time.year for r in records) - min(r.time.year for r in records)} years.')

# Which airport had the most carriers at any point of the year?
most_carriers = max(records, key=lambda r: len(r.statistics.carriers))
print(f'The maximum number of carriers:')

for r in [rec for rec in records if len(rec.statistics.carriers) == len(most_carriers.statistics.carriers)]:
    print(f'{r.airport.code} ({r.time.label}) - {len(r.statistics.carriers)}')

# List all the carriers present in the dataset
carriers = set()
for r in records:
    carriers.update(r.statistics.carriers)

print(f'Carriers in the dataset {len(carriers)}')

# What is the total number of canceled flights?
print(f'The total number of canceled flights is: {sum(r.statistics.canceled for r in records):,}')

# What is the average delay time due to late aircraft?
print(
    f'The average delay due to late aircraft was around {sum(r.statistics.delay_minutes_late_aircraft for r in records) / len(records) / 30:.0f} minutes per day.')

# Which airport was the most precise overall (highest percentage on time)?
# airport code -> [records of the airport]
airports = defaultdict(list)

for r in records:
    airports[r.airport.code].append(r)


def ratio(t):
    k, v = t
    return sum(r.statistics.on_time for r in v) / sum(r.statistics.total_flights for r in v)


most_precise = max(airports.items(), key=ratio)
print(
    f'The code of the most precise airport is {most_precise[0]}, which had an average of {ratio(most_precise) * 100:.2f}% of flights on time.')

airports = list(airports.items())
airports.sort(key=ratio, reverse=True)
print('Precision by airports:')
for t in airports:
    print(f'{t[0]}: {ratio(t) * 100:.2f}%')
