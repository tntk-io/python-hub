# Mutable And Immutatble Data Types

## Copy values of a list

Given a list l1:

`l1 = [1, 2, 3]`

Create a new list `l2` and copy the values of `l1` (do not create a reference to `l1`).

Set the first element of `l1` to `0`.

To ensure that you copied the values and not just created a reference, check that the two lists are not equal to each other by running:

`print(l1 != l2)`

If you did the exercise correctly, the console will print True.

## Update datetime

Given a datetime in the form of a tuple:

`date = 2000, 11, 18`

"Update" the year part to `2024`. Since tuples are immutable, of course, the tuple will have to be recreated to achieve this.

## Date => event dictionary

Given the following list of datetimes and their corresponding events create a dictionary, where the keys are the datetimes and the values are the events.

```
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
```

## Censor string

Given the following string, replace every vowel with an underscore.

`text = 'Lorem ipsum dolor sit amet'`

