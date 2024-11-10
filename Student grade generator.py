# Student Grade Generator

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def generate_grades(students_scores):
    grades = {}
    for student, score in students_scores.items():
        grades[student] = get_grade(score)
    return grades

# Sample data: dictionary with student names and their scores
students_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 65,
    "Edward": 54
}

# Generate and display grades
grades = generate_grades(students_scores)
print("Student Grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")
