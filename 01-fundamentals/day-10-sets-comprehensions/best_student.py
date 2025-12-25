marks = {"Aayush": 85, "Raj" : 92, "Giri": 78}

best_student = ""
max_marks = -1

for student, marks in marks.items():
    if marks > max_marks:
        max_marks = marks
        best_student =  student

print(f"The best student is {best_student} with marks {max_marks}")
