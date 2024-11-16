from collections import Counter, defaultdict

print('Most common name (without built-in functions)')
names = [
    "Alice", "Bob", "Alice", "Charlie", "David", "Alice", "Eve",
    "Alice", "Frank", "Charlie", "Alice", "Eve", "Bob", "Alice",
    "Grace", "David", "Bob", "Alice", "Charlie", "Alice", "Eve",
    "Alice", "Bob", "Alice", "David", "Alice", "Charlie", "Alice",
    "Eve", "Alice"
]

records = {}
for name in names:
    # Check if the record does not exist in the dictionary
    if name not in records:
        # Add the name and initialize at 1 (since this is the first occurrence)
        records[name] = 1
    # Otherwise (if the name is in the dictionary)
    else:
        # Increment the occurrence of the name by one
        records[name] += 1  # records[name] = records[name] + 1

# The number of times the most common name occurred and the most common name
# highest_occurrence[0] = the number of times the name occurred
# highest_occurrence[1] = the most common name
highest_occurrence = 0, ''

for name, occurrence in records.items():
    if occurrence > highest_occurrence[0]:
        highest_occurrence = occurrence, name

print('The most common name is', highest_occurrence[1])

print('Most common name (with built-in functions)')

# Create a frequency table
records = Counter(names)
# Select the first most common (name, frequency), then the name of that
print('The most common name is', records.most_common()[0][0])

# In case you don't remember the most_common function, you can use a lambda function to compare by the frequency
highest = max(records.items(), key=lambda t: t[1])
print('The most common name is', highest[0])

print('Total number of enrollments')
courses = [
    {'Number of classes': 7, 'Students per class': 24, 'Course': 'Biology'},
    {'Number of classes': 10, 'Students per class': 30, 'Course': 'Mathematics'},
    {'Number of classes': 5, 'Students per class': 22, 'Course': 'History'},
    {'Number of classes': 14, 'Students per class': 26, 'Course': 'Physical Education'},
    {'Number of classes': 9, 'Students per class': 20, 'Course': 'Computer Science'}
]

# Total number of enrollments
total = 0
for course in courses:
    total += course['Number of classes'] * course['Students per class']  # Number of enrollments per course

print(total, 'enrollments')

# Using sum
print(sum(course['Number of classes'] * course['Students per class'] for course in courses), 'enrollments')

print('Cities with the largest and smallest population')

populations = [
    ("Tokyo", 13929286), ("Delhi", 30290936), ("Shanghai", 24870895), ("São Paulo", 12325232), ("Mumbai", 20411000),
    ("Mexico City", 9209944), ("Cairo", 20040800), ("Dhaka", 22025000), ("Osaka", 19222665), ("New York City", 8419600),
    ("Karachi", 14910352), ("Istanbul", 15462452), ("Chengdu", 16330000), ("Los Angeles", 3980400),
    ("Bangkok", 10410000),
    ("Kolkata", 14930000), ("Nairobi", 4397087), ("London", 8982000), ("Rio de Janeiro", 6748000),
    ("Hong Kong", 7496981)
]

# Initializing it as the first element
highest = populations[0]
lowest = populations[0]

for p in populations:
    name, population = p[0], p[1]
    if population > highest[1]:
        highest = name, population
    if population < lowest[1]:
        lowest = name, population

print('Highest:', highest[0])
print('Lowest:', lowest[0])

# Using lambda expressions along with the max/min functions
print('Highest:', max(populations, key=lambda t: t[1])[0])
print('Lowest:', min(populations, key=lambda t: t[1])[0])

print('Average speeds')

car_speeds = [
    ("Chevrolet", 90), ("Toyota", 97), ("BMW", 120), ("Ford", 105), ("Honda", 82),
    ("Toyota", 83), ("Honda", 99), ("Chevrolet", 100), ("Ford", 110), ("BMW", 115),
    ("Toyota", 89), ("Chevrolet", 98), ("Ford", 108), ("Honda", 86), ("BMW", 119),
    ("Ford", 120), ("Toyota", 78), ("Honda", 85), ("Chevrolet", 92), ("BMW", 114),
    ("Honda", 88), ("Toyota", 95), ("Ford", 112), ("BMW", 111), ("Chevrolet", 93),
]

cars = {}
for brand, speed in car_speeds:
    if brand not in cars:
        cars[brand] = [speed]
    else:
        cars[brand].append(speed)

for brand in cars:
    cars[brand] = sum(cars[brand]) / len(cars[brand])

print('Average speeds:', cars)

# Using default dict
cars = defaultdict(list)
for brand, speed in car_speeds:
    cars[brand].append(speed)

for brand in cars:
    cars[brand] = sum(cars[brand]) / len(cars[brand])

print('Average speeds:', cars)
print('Highest average speed:', max(cars.items(), key=lambda t: t[1])[0])
