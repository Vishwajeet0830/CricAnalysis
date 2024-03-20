import numpy as np
import random

class Student:
    def __init__(self, name: str):
        self.name = name
        self._cwid = self._generate_cwid()
        self._grades = self._generate_grades()

    def _generate_cwid(self) -> str:
        first_digit = random.randint(1, 9)
        other_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return f"{first_digit}{other_digits}"

    def _generate_grades(self):
        grades = [grade for grade in self._generate_grade()]
        while len(grades) < 10:
            grades.append(np.nan)
        return grades

    def _generate_grade(self):
        while True:
            grade = random.choice([4.0, 3.0, 2.0, 1.0, np.nan])
            if grade != np.nan or len(self._grades) >= 8:
                yield grade

    def __str__(self) -> str:
        valid_grades = [str(grade) for grade in self._grades if grade != np.nan]
        return f"{self.name} ({self._cwid}): {valid_grades}"

def simulate_students():
    student_names = ["Messi", "Ronaldo", "Neymar", "Benzema", "Salah", "Suarez", "Haaland", "Bruno", "Eric", "Busquets"]
    students = [Student(name) for name in student_names]
    return students

def calculate_gpa(students):
    credit_hours = 3
    gpa_list = []
    for student in students:
        valid_grades = [grade for grade in student._grades if grade != np.nan]
        total_points = sum(valid_grades) * credit_hours
        total_courses = len(valid_grades)
        gpa = total_points / (total_courses * credit_hours)
        gpa_list.append(gpa)
    return np.array(gpa_list)

def find_best_students(students):
    gpas = calculate_gpa(students)
    top_indices = np.argsort(gpas)[-3:]
    best_students = []
    for idx in top_indices:
        if len([grade for grade in students[idx]._grades if grade != np.nan]) >= 6:
            best_students.append(students[idx])
    print("Top 3 Students with highest GPA who took at least 6 courses:")
    for student in best_students:
        print(student)

def find_risky_students(students):
    risky_students = sorted(students, key=lambda x: x._grades.count(2.0) + x._grades.count(1.0), reverse=True)
    risky_students = [student for student in risky_students if student._grades.count(2.0) + student._grades.count(1.0) >= 2]
    print("Risky Students:")
    for student in risky_students:
        print(student)

if __name__ == "__main__":
    students = simulate_students()
    print("Generated Students:")
    for student in students:
        print(student)
    print("GPA of all students:", calculate_gpa(students))
    find_best_students(students)
    find_risky_students(students)

