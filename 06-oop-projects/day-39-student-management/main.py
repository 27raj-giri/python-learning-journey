from student_system import Person, Student, GraduateStudent, School

def main():
    school = School("Tech Institute of India")
    
    while True:
        print("\n" + "="*40)
        print("STUDENT MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Undergraduate Student")
        print("2. Add Graduate Student")
        print("3. Add Grade to Student")
        print("4. Display All Students")
        print("5. Display Student Report")
        print("6. Submit Thesis (Graduate Only)")
        print("7. School Statistics")
        print("8. Exit")
        print("="*40)
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            student_id = input("Enter student ID: ").strip()
            grade_level = input("Enter grade level (9-12 or Freshman/Sophomore/etc): ").strip()
            
            student = Student(name, age, student_id, grade_level)
            school.add_student(student)
        
        elif choice == '2':
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            student_id = input("Enter student ID: ").strip()
            degree_type = input("Degree type (Masters/PhD): ").strip()
            thesis_topic = input("Thesis topic: ").strip()
            advisor = input("Advisor name: ").strip()
            
            grad_student = GraduateStudent(name, age, student_id, degree_type, thesis_topic, advisor)
            school.add_student(grad_student)
        
        elif choice == '3':
            name = input("Enter student name: ").strip()
            student = school.find_student(name)
            
            if student:
                course = input("Enter course name: ").strip()
                try:
                    grade = float(input("Enter grade (0-100): "))
                    student.add_grade(course, grade)
                except ValueError:
                    print("Grade must be a number")
            else:
                print("Student not found")
        
        elif choice == '4':
            school.display_all_students()  # Polymorphism in action!
        
        elif choice == '5':
            name = input("Enter student name: ").strip()
            student = school.find_student(name)
            
            if student:
                student.display_info()  # Polymorphism!
            else:
                print("✗ Student not found")
        
        elif choice == '6':
            name = input("Enter graduate student name: ").strip()
            student = school.find_student(name)
            
            if student and isinstance(student, GraduateStudent):
                student.submit_thesis()
            elif student:
                print("✗ Only graduate students can submit thesis")
            else:
                print("✗ Student not found")
        
        elif choice == '7':
            school.show_statistics()
        
        elif choice == '8':
            print("\nThank you for using the system. Goodbye! 🎓")
            break
        
        else:
            print("✗ Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()