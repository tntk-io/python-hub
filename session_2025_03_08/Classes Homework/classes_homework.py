from random import randint


class Student:
    def __init__(self, name, birth_year, university, major=None):
        self.name = name
        self.birth_year = birth_year
        self.university = university
        self.major = major
        self.grades = []

    def add_grades(self, *grades):
        self.grades.extend(grades)

    @property
    def gpa(self):
        return sum(self.grades) / len(self.grades)

    def change_birth_year(self, year):
        # abs(self.birth_year - year) <= 5 # Alternatively
        if -5 <= self.birth_year - year <= 5:
            self.birth_year = year
            return True
        return False


students = [
    Student('Deng Xiaoping', 1904, 'Moscow Sun Yat-sen University'),
    Student('Jiang Zemin', 1926, 'Shanghai Jiao Tong University', 'Electrical Engineering'),
    Student('Hu Jintao', 1942, 'Tsinghua University', 'Hydraulic Engineering')
]

for s in students:
    if s.change_birth_year(1930):
        print(f'Successfully updated the birth year of {s.name} to {s.birth_year}')
    else:
        print(f'Could not update the birth year of {s.name} to 1930.')

# for s in students:
#     if s.major is None:
#         print(f'The student with no major is: {s.name}')
#         break

student_with_no_major = next((s for s in students if s.major is None), None)
if student_with_no_major:
    print(f'The student with no major is: {student_with_no_major.name}')

for s in students:
    # Number of grades the students will have
    grades = [randint(0, 10) for i in range(randint(5, 10))]
    s.add_grades(*grades)
    print(f'{s.name} - {", ".join(str(g) for g in s.grades)} - {s.gpa}')
