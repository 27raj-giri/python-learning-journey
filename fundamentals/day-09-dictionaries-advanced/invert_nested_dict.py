school = {
    "Class A": ["Aayush", "Raj", "Giri"],
    "Class B": ["Raj", "Aashu", "Potla"]
}

inverted = {}

for class_name, students in school.items():
    for student in students:
        inverted.setdefault(student, [])
        inverted[student].append(class_name)

print(inverted)
