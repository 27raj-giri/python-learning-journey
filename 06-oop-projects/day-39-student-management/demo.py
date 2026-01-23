"""
Automated demo showing inheritance and polymorphism in action
"""

from student_system import Person, Student, GraduateStudent, School

def main():
    print("="*60)
    print("STUDENT MANAGEMENT SYSTEM - INHERITANCE & POLYMORPHISM DEMO")
    print("="*60)
    
    # Create school
    school = School("Tech Institute of India")
    print(f"\n🎓 {school.name} initialized!\n")
    
    # Test 1: Add undergraduate students
    print("="*60)
    print("TEST 1: Adding Undergraduate Students")
    print("-"*60)
    student1 = Student("Raj Kumar", 20, "UG001", "Junior")
    student1.add_grade("Data Structures", 85)
    student1.add_grade("Algorithms", 90)
    student1.add_grade("Databases", 88)
    school.add_student(student1)
    
    student2 = Student("Priya Sharma", 19, "UG002", "Sophomore")
    student2.add_grade("Python Programming", 92)
    student2.add_grade("Web Development", 87)
    school.add_student(student2)
    
    # Test 2: Add graduate students
    print("\n" + "="*60)
    print("TEST 2: Adding Graduate Students")
    print("-"*60)
    grad1 = GraduateStudent("Aayush Raj Giri", 21, "GRAD001", "Masters", 
                           "AI in Healthcare", "Dr. Sharma")
    grad1.add_grade("Machine Learning", 95)
    grad1.add_grade("Deep Learning", 93)
    school.add_student(grad1)
    
    grad2 = GraduateStudent("Sneha Patel", 24, "GRAD002", "PhD", 
                           "Quantum Computing", "Dr. Verma")
    grad2.add_grade("Quantum Algorithms", 94)
    school.add_student(grad2)
    
    # Test 3: Polymorphic display (IMPORTANT!)
    print("\n" + "="*60)
    print("TEST 3: POLYMORPHIC DISPLAY")
    print("(Notice: Same method, different behavior!)")
    print("-"*60)
    school.display_all_students()
    
    # Test 4: Graduate-specific functionality
    print("="*60)
    print("TEST 4: Graduate-Specific Methods")
    print("-"*60)
    grad1.submit_thesis()
    grad2.submit_thesis()
    
    # Test 5: School statistics
    print("="*60)
    print("TEST 5: School Statistics")
    print("-"*60)
    school.show_statistics()
    
    # Test 6: Search and display (polymorphism again)
    print("="*60)
    print("TEST 6: Individual Student Display (Polymorphism)")
    print("-"*60)
    found = school.find_student("Aayush")
    if found:
        found.display_info()  # Calls GraduateStudent version
    
    found = school.find_student("Raj")
    if found:
        found.display_info()  # Calls Student version
    
    print("="*60)
    print("ALL TESTS COMPLETED!")
    print("="*60)
    print("\nKey OOP Concepts Demonstrated:")
    print("  Inheritance: Person → Student → GraduateStudent")
    print("  Polymorphism: display_info() works differently for each class")
    print("  Method Overriding: Each class customizes display_info()")
    print("  super(): Calling parent class methods")
    print("  isinstance(): Checking object types")
    print("="*60)

if __name__ == "__main__":
    main()