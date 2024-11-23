import csv
from collections import Counter, defaultdict

data = []

with open('coffee.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line in reader:
        data.append(line)

print('The most common country was', Counter(d['Location.Country'] for d in data).most_common()[0][0])
print('The most common color of coffee beans was', Counter(d['Data.Color'] for d in data).most_common()[0][0])
highest_country = max(data, key=lambda d: int(d['Location.Altitude.Average']))
print('The highest country based on average altitude was', highest_country['Location.Country'])


# How much was the overall output (number of bags × weight)?
def total_output(data):
    total = 0
    for record in data:
        total += int(record['Data.Production.Number of bags']) * float(record['Data.Production.Bag weight'])
    return total


print(f'Total output: {total_output(data)} kg (?)')


# Which one was sweeter on average, Arabica or Robusta?
def sweetest_variety(data):
    sweetness = defaultdict(list)
    for record in data:
        sweetness[record['Data.Type.Species']].append(float(record['Data.Scores.Sweetness']))

    for key, value in sweetness.items():
        sweetness[key] = sum(value) / len(value)

    sweetest_species = max(sweetness.items(), key=lambda t: t[1])
    return sweetest_species[0]


print(f'{sweetest_variety(data)} is the sweetest species')


# Processing methods using for loop and default dict
def frequency_of_processing_methods(data):
    processing_methods = defaultdict(int)
    for record in data:
        method = record['Data.Type.Processing method']
        if method == 'nan':
            processing_methods['Other'] += 1
        else:
            processing_methods[method] += 1
    return processing_methods


print('Processing methods', frequency_of_processing_methods(data))


# Processing methods using Counter
def frequency_of_processing_methods_using_counter(data):
    methods = [record['Data.Type.Processing method'] for record in data]
    d = Counter(methods)
    d['Other'] += d['nan']
    del d['nan']
    return d


print('Processing methods', frequency_of_processing_methods_using_counter(data))


# Processing methods without default dict
def frequency_of_processing_methods_using_builtins(data):
    processing_methods = {}
    for record in data:
        method = record['Data.Type.Processing method']
        if method == 'nan':
            method = 'Other'

        if method not in processing_methods:
            processing_methods[method] = 1
        else:
            processing_methods[method] += 1
    return processing_methods


print('Processing methods', frequency_of_processing_methods_using_builtins(data))


# List the variety of the top and the bottom 5 coffee beans by total score
def varieties_by_score(data):
    varieties = defaultdict(list)
    for record in data:
        varieties[record['Data.Type.Variety']].append(float(record['Data.Scores.Total']))

    for key, value in varieties.items():
        varieties[key] = sum(value) / len(value)

    varieties = list(varieties.items())
    varieties.sort(key=lambda t: t[1])
    return varieties


def top_varieties(data, n):
    return [t[0] for t in varieties_by_score(data)[:n]]


def bottom_varieties(data, n):
    return [t[0] for t in varieties_by_score(data)[-n:]]


print('Top five:', ', '.join(top_varieties(data, 5)))
print('Bottom five:', ', '.join(bottom_varieties(data, 5)))

# Show the number of countries cultivating coffee beans
print(len({record['Location.Country'] for record in data}), 'countries were recorded in the dataset')


# Which country produced the most bags of coffee and how many?
def country_producing_most_bags(data):
    countries = defaultdict(int)
    for record in data:
        countries[record['Location.Country']] += int(record['Data.Production.Number of bags'])

    countries = list(countries.items())
    country_producing_most_bags = max(countries, key=lambda t: t[1])
    return country_producing_most_bags[0]


print('The country that produced the most bags of coffee is', country_producing_most_bags(data))
