# Copy values of a list
l1 = [1, 2, 3]
l2 = list(l1)
l1[0] = 0
print(l1, l2)
print(l1 != l2)

# Update datetime
date = 2000, 11, 18
date = 2024, date[1], date[2]
print(date)

# Date => events dictionary
datetimes = [
    (2024, 11, 18),
    (2023, 12, 25),
    (2020, 1, 1),
    (1999, 12, 31),
    (2005, 6, 15),
    (2010, 7, 4),
    (2022, 8, 12),
    (1987, 3, 22),
    (2015, 11, 11),
    (2021, 2, 14)
]

events = [
    "Current date",
    "Christmas 2023",
    "New Year 2020",
    "New Year's Eve 1999",
    "Random date",
    "Independence Day 2010 (US)",
    "Random summer date",
    "Random historical date",
    "Veterans Day 2015 (US)",
    "Valentine's Day 2021"
]

d = dict(zip(datetimes, events))
print(d)

# Letter => position in alphabet
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
positions = list(range(1, len(alphabet) + 1))
print(alphabet)
print(positions)
d = dict(zip(alphabet, positions))
print(d)

# Manually
d = {}
for i in range(len(alphabet)):
    d[alphabet[i]] = positions[i]

print(d)

# Censor string using for loop
vowels = 'aeiou'
text = 'Lorem ipsum dolor sit amet'
text = list(text)

for i in range(len(text)):
    if text[i].lower() in vowels:
        text[i] = '_'

text = ''.join(text)
print(text)

# Censor string using list comprehension
text = 'Lorem ipsum dolor sit amet'
vowels = set('aeiou')
text = ''.join('_' if c.lower() in vowels else c for c in text)
print(text)
