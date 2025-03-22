from collections import Counter

names = [
    "Alice", "Bob", "Alice", "Charlie", "David", "Alice", "Eve",
    "Alice", "Frank", "Charlie", "Alice", "Eve", "Bob", "Alice",
    "Grace", "David", "Bob", "Alice", "Charlie", "Alice", "Eve",
    "Alice", "Bob", "Alice", "David", "Alice", "Charlie", "Alice",
    "Eve", "Alice"
]
print('Most common name:', Counter(names).most_common(1)[0][0])

# Highest average speed
car_speeds = [
    ("Chevrolet", 90), ("Toyota", 97), ("BMW", 120), ("Ford", 105), ("Honda", 82),
    ("Toyota", 83), ("Honda", 99), ("Chevrolet", 100), ("Ford", 110), ("BMW", 115),
    ("Toyota", 89), ("Chevrolet", 98), ("Ford", 108), ("Honda", 86), ("BMW", 119),
    ("Ford", 120), ("Toyota", 78), ("Honda", 85), ("Chevrolet", 92), ("BMW", 114),
    ("Honda", 88), ("Toyota", 95), ("Ford", 112), ("BMW", 111), ("Chevrolet", 93),
]
d = {}
for t in car_speeds:
    if t[0] not in d:
        d[t[0]] = [t[1]]
    else:
        d[t[0]].append(t[1])

found = max([(sum(d[brand]) / len(d[brand]), brand) for brand in d], key=lambda t: t[0])
print('Brand with fastest recorded speed:', found[1])

classes = [
    {'Number of classes': 7, 'Students per class': 24, 'Course': 'Biology'},
    {'Number of classes': 10, 'Students per class': 30, 'Course': 'Mathematics'},
    {'Number of classes': 5, 'Students per class': 22, 'Course': 'History'},
    {'Number of classes': 14, 'Students per class': 26, 'Course': 'Physical Education'},
    {'Number of classes': 9, 'Students per class': 20, 'Course': 'Computer Science'}
]

total = 0
for c in classes:
    total += c['Number of classes'] * c['Students per class']

print('The total number of enrollments is:', total)

populations = [
    ("Tokyo", 13929286), ("Delhi", 30290936), ("Shanghai", 24870895), ("São Paulo", 12325232), ("Mumbai", 20411000),
    ("Mexico City", 9209944), ("Cairo", 20040800), ("Dhaka", 22025000), ("Osaka", 19222665), ("New York City", 8419600),
    ("Karachi", 14910352), ("Istanbul", 15462452), ("Chengdu", 16330000), ("Los Angeles", 3980400),
    ("Bangkok", 10410000),
    ("Kolkata", 14930000), ("Nairobi", 4397087), ("London", 8982000), ("Rio de Janeiro", 6748000),
    ("Hong Kong", 7496981)
]
print('Smallest:', min(populations, key=lambda t: t[1])[0])
print('Largest:', max(populations, key=lambda t: t[1])[0])
