# Classes Homework

## Student

Create a `Student` class that stores the `name`, the `birth_year`, the `university` and optionally the `major` of a student.
It should also have a `grades` array that is initialized as an empty array.

Create an `add_grades` method that takes [arbitrarily many grades](https://www.geeksforgeeks.org/args-kwargs-python/) and adds them to the `grades` attribute of `Student`.

Create a property called `gpa` that returns the `gpa` of the students (average of their grades).

Create a method called `change_birth_year` which takes `year` as a parameter.
It should only allow the student to change their birth year by maximum of 5 years interval inclusively (either before or after the original).
Return `True` if successful, otherwise return `False`.

After creating the classes, try to run the following code to store the students. Adjust your code if needed.

```
students = [
    Student('Deng Xiaoping', 1904, 'Moscow Sun Yat-sen University'),
    Student('Jiang Zemin', 1926, 'Shanghai Jiao Tong University', 'Electrical Engineering'),
    Student('Hu Jintao', 1942, 'Tsinghua University', 'Hydraulic Engineering')
]
```

## Change birth years

Try to change the birth year of each student to 1930.
Print their names along with their birth year after the change.
If it fails, report that back to the user.

## No major

Iterate through the students and display the name and university of students that do not have a known major.

## Store grades

Iterate through the array and store 5 to 10 grades for each of them, ranging from 0 to 10.
You can use the `randint` function from the `random` module for this purpose.

## GPA

Print the names, the grades and the gpa of the students in the following format:

`name - grade1, grade2, ..., grade10 - gpa`