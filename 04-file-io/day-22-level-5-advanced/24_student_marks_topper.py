# Find the Topper (Student Marks)

with open("marks.txt", "r") as f:
    max_marks = 0
    topper_name = ""

    for line in f:
        name, marks = line.strip().split(",")
        marks = int(marks)

        if marks > max_marks:
            max_marks = marks
            topper_name = name

print(f"Topper is {topper_name} with {max_marks} marks")