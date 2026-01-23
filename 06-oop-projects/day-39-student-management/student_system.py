class Person:
    """Base class representing any person in the system"""
    
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id
    
    def display_info(self):
        """Display basic person information - to be overridden"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")


class Student(Person):
    """Undergraduate student class - inherits from Person"""
    
    def __init__(self, name, age, student_id, grade_level):
        super().__init__(name, age, student_id)
        self.grade_level = grade_level
        self.grades = {}
    
    def add_grade(self, course, grade):
        """Add a grade for a course"""
        self.grades[course] = grade
        print(f"Added: {course} - {grade}")
    
    def calculate_gpa(self):
        """Calculate GPA from all grades"""
        if not self.grades:
            return 0.0
        return round(sum(self.grades.values()) / len(self.grades), 2)
    
    def display_info(self):
        """Override parent method - polymorphism in action"""
        print(f"\n{'='*40}")
        print(f"UNDERGRADUATE STUDENT")
        print(f"{'='*40}")
        super().display_info()
        print(f"Grade Level: {self.grade_level}")
        print(f"Total Courses: {len(self.grades)}")
        print(f"GPA: {self.calculate_gpa()}")
        
        if self.grades:
            print("\nGrades:")
            for course, grade in self.grades.items():
                print(f"  • {course}: {grade}")
        print(f"{'='*40}\n")


class GraduateStudent(Student):
    """Graduate student class - inherits from Student"""
    
    def __init__(self, name, age, student_id, degree_type, thesis_topic, advisor):
        super().__init__(name, age, student_id, "Graduate")
        self.degree_type = degree_type
        self.thesis_topic = thesis_topic
        self.advisor = advisor
    
    def display_info(self):
        """Override again - multilevel polymorphism"""
        print(f"\n{'='*40}")
        print(f"GRADUATE STUDENT ({self.degree_type})")
        print(f"{'='*40}")
        Person.display_info(self)
        print(f"Degree Program: {self.degree_type}")
        print(f"Thesis Topic: {self.thesis_topic}")
        print(f"Advisor: {self.advisor}")
        print(f"GPA: {self.calculate_gpa()}")
        
        if self.grades:
            print("\nCourses:")
            for course, grade in self.grades.items():
                print(f"  • {course}: {grade}")
        print(f"{'='*40}\n")
    
    def submit_thesis(self):
        """Graduate-specific method"""
        print(f"\n{self.name} submitted thesis:")
        print(f"  Topic: '{self.thesis_topic}'")
        print(f"  Advisor: {self.advisor}\n")


class School:
    """School management system - demonstrates polymorphism"""
    
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        """Add any type of student (polymorphism)"""
        self.students.append(student)
        student_type = "Graduate" if isinstance(student, GraduateStudent) else "Undergraduate"
        print(f"{student.name} enrolled as {student_type} student")
    
    def display_all_students(self):
        """Display all students - polymorphic display"""
        print(f"\n{'='*50}")
        print(f"{self.name.upper()} - STUDENT DIRECTORY")
        print(f"{'='*50}")
        
        if not self.students:
            print("(No students enrolled)")
        else:
            for student in self.students:
                
                student.display_info()
        
        print(f"{'='*50}\n")
    
    def find_student(self, name):
        """Search for student by name"""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None
    
    def show_statistics(self):
        """Display school statistics"""
        undergrad = sum(1 for s in self.students if not isinstance(s, GraduateStudent))
        grad = sum(1 for s in self.students if isinstance(s, GraduateStudent))
        
        print(f"\n{self.name} - Statistics")
        print(f"Total Students: {len(self.students)}")
        print(f"  • Undergraduate: {undergrad}")
        print(f"  • Graduate: {grad}\n")