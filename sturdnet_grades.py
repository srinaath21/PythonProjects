students_grades = {
    "Srinaath" : 91,
    "Keerthi" : 92,
    "Siva" : 77,
    "Yuvaraj" : 65,
    "Yoshva": 88,
}

for students in students_grades:
    score = students_grades[students]
    if score > 90 and score <= 100:
        students_grades[students] = "Outstanding"
    elif score > 80 and score <= 90:
        students_grades[students] = "Exceeding Expectations"
    elif score > 70 and score <= 80:
        students_grades[students] = "Acceptable"
    else :
        students_grades[students] = "Fail"

print(students_grades)