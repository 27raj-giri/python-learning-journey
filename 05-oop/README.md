# 05-oop - Object-Oriented Programming

**Duration:** Days 24-39 (16 days)  
**Programs:** 39 programs  
**Date:** January 8-23, 2026  
**Status:** 🔄 In Progress

---

## 📖 OVERVIEW

Complete Object-Oriented Programming (OOP) module covering classes, objects, inheritance, encapsulation, and polymorphism. Built during exam period with strategic daily practice.

**Learning Approach:** Progressive difficulty from basic classes to complete mini-projects

---

## 📂 FOLDER STRUCTURE
```
05-oop/
│
├── README.md (this file)
│
├── day-24-classes-basics/          (4 programs)
├── day-25-init-constructor/        (4 programs)
├── day-26-methods-basic/           (4 programs)
├── day-27-methods-advanced/        (4 programs)
│
├── day-28-inheritance-basics/      (3 programs)
├── day-29-inheritance-super/       (3 programs)
├── day-30-inheritance-multilevel/  (3 programs)
├── day-31-inheritance-advanced/    (3 programs)
├── day-32-inheritance-complete/    (2 programs)
│
├── day-33-encapsulation-basics/    (3 programs)
├── day-34-encapsulation-advanced/  (3 programs)
│
├── day-35-polymorphism-basics/     (3 programs)
└── day-36-polymorphism-operators/  (2 programs)
│
└── mini-projects/
    ├── day-37-library-system/      (1 project)
    ├── day-38-bank-system/         (1 project)
    └── day-39-student-management/  (1 project)
```

---

## 🎯 LEARNING OBJECTIVES

By the end of this module, I will master:

✅ **Classes & Objects**
- Creating classes and objects
- Constructor and initialization
- Instance variables
- Self parameter

✅ **Methods**
- Instance methods
- Parameters and return values
- Getters and setters
- Class variables

✅ **Inheritance**
- Parent-child relationships
- Code reusability
- Super keyword usage
- Multilevel inheritance
- Method overriding

✅ **Encapsulation**
- Data hiding
- Private variables
- Protected variables
- Access control

✅ **Polymorphism**
- Method overriding
- Operator overloading
- Same interface, different behavior

---

## 📚 MODULE BREAKDOWN

### **WEEK 1: Classes & Methods (Days 24-27)**

#### **Day 24 - Classes Basics**
**Programs:** 4  
**Focus:** First classes, object creation

**Topics Covered:**
- Class definition
- Object instantiation
- Constructor basics
- Self parameter understanding

**Programs:**
1. Person class with name and age
2. Rectangle class with area method
3. Circle class with area and circumference
4. Student class with display method

---

#### **Day 25 - Init Constructor**
**Programs:** 4  
**Focus:** Constructor usage, multiple objects

**Topics Covered:**
- Automatic initialization
- Setting default values
- Creating multiple objects
- Different data per object

**Programs:**
5. Book class with title, author, price
6. Car class with brand, model, year
7. Bank account with balance
8. Temperature class (Celsius to Fahrenheit)

---

#### **Day 26 - Methods Basic**
**Programs:** 4  
**Focus:** Methods with parameters, return values

**Topics Covered:**
- Methods with parameters
- Return value handling
- Class variables introduction
- Private variables basics

**Programs:**
9. Calculator class with 4 operations
10. Counter class with increment/decrement
11. Student with private marks
12. Product with total count tracking

---

#### **Day 27 - Methods Advanced**
**Programs:** 4  
**Focus:** Getters, setters, method interactions

**Topics Covered:**
- Getter methods
- Setter methods with validation
- Methods calling other methods
- Boolean return values

**Programs:**
13. Employee with salary calculation
14. Time class with formatting
15. String manipulator class
16. Movie with rating check

---

### **WEEK 2: Inheritance (Days 28-32)**

#### **Day 28 - Inheritance Basics**
**Programs:** 3  
**Focus:** Parent-child classes, code reuse

**Topics Covered:**
- Parent class (base class)
- Child class (derived class)
- Inheriting properties
- Inheriting methods

**Programs:**
17. Animal parent, Dog child
18. Vehicle parent, Car child
19. Shape hierarchy with Rectangle, Circle

---

#### **Day 29 - Inheritance with Super**
**Programs:** 3  
**Focus:** Super keyword, parent access

**Topics Covered:**
- Super keyword usage
- Calling parent constructor
- Extending parent functionality
- Adding child-specific features

**Programs:**
20. Person → Student inheritance
21. Employee → Manager inheritance
22. Demonstrating super keyword

---

#### **Day 30 - Multilevel Inheritance**
**Programs:** 3  
**Focus:** Inheritance chains, multiple levels

**Topics Covered:**
- Multilevel inheritance
- Inheritance chains
- Method overriding
- Customizing behavior

**Programs:**
23. GrandParent → Parent → Child
24. Bank accounts (Account → Savings/Current)
25. Bird → Penguin (method overriding)

---

#### **Day 31 - Inheritance Advanced**
**Programs:** 3  
**Focus:** Complex hierarchies, real scenarios

**Topics Covered:**
- Deep inheritance chains
- Adding features at each level
- Permission/privilege patterns
- Real-world hierarchies

**Programs:**
26. Phone → Smartphone
27. Vehicle → Car → ElectricCar
28. User → Admin (privileges)

---

#### **Day 32 - Inheritance Complete**
**Programs:** 2  
**Focus:** Final inheritance concepts

**Topics Covered:**
- Specialized classes
- Different behaviors per type
- Inheritance summary
- When to use inheritance

**Programs:**
29. Product → ElectronicProduct
30. Account types with different rules

---

### **WEEK 3: Encapsulation & Polymorphism (Days 33-36)**

#### **Day 33 - Encapsulation Basics**
**Programs:** 3  
**Focus:** Data hiding, private variables

**Topics Covered:**
- Private variables
- Data hiding principles
- Getters for access
- Setters with validation

**Programs:**
31. Bank account with private balance
32. Person with age validation
33. Password class with verification

---

#### **Day 34 - Encapsulation Advanced**
**Programs:** 3  
**Focus:** Access levels, security

**Topics Covered:**
- Public, protected, private access
- Security patterns
- Controlled modification
- Validation logic

**Programs:**
34. Student with access level demo
35. ATM with PIN security
36. Car with fuel management

---

#### **Day 35 - Polymorphism Basics**
**Programs:** 3  
**Focus:** Same method, different behavior

**Topics Covered:**
- Method overriding
- Same interface, different implementation
- Polymorphic behavior
- Flexibility in design

**Programs:**
37. Shape polymorphism (different areas)
38. Payment methods (different processing)
39. Animal sounds (different sounds)

---

#### **Day 36 - Operator Overloading**
**Programs:** 2  
**Focus:** Custom operators

**Topics Covered:**
- Operator overloading
- Magic methods (add, sub, etc.)
- Comparison operators (lt, gt, eq)
- Custom behavior for operators

**Programs:**
40. Point addition (overload +)
41. Distance comparison (overload <, >, ==)

---

## 🚀 MINI PROJECTS (Days 37-39)

### **Day 37 - Library Management System**
**Date:** January 21, 2026  
**Duration:** ~2-3 hours  
**File:** `library_system.py`

**Features:**
- Book class with title, author, ISBN, availability
- Library class for managing books
- Add, lend, and return book functionality
- Member tracking system
- Search functionality
- Availability status checking

**Concepts Applied:**
- Multiple classes working together
- Lists for data storage
- Method interactions between classes
- Real-world business logic
- Data validation

**Learning Outcome:**  
First complete application using OOP principles!

---

### **Day 38 - Bank Account System**
**Date:** January 22, 2026  
**Duration:** ~2-3 hours  
**File:** `bank_system.py`

**Features:**
- Account class with deposit, withdraw, transfer
- Balance management with encapsulation
- Transaction history tracking
- Error handling for invalid operations
- Inter-account transfers
- PIN-based security

**Concepts Applied:**
- Encapsulation (private balance)
- Method validation and error handling
- Inter-object operations
- Security patterns
- Transaction logging

**Learning Outcome:**  
Secure financial application with proper validation!

---

### **Day 39 - Student Management System**
**Date:** January 23, 2026  
**Duration:** ~2-3 hours  
**File:** `student_management.py`

**Features:**
- Student class with name, grades, courses
- Course enrollment system
- GPA calculation functionality
- Grade management (add, update, remove)
- Report generation
- Student search and filtering

**Concepts Applied:**
- Multiple class interactions
- Grade calculations and averaging
- List management for courses
- Report formatting
- Data organization

**Learning Outcome:**  
Complete academic management system with calculations!

---

## 📊 PROGRESS TRACKING

### **Statistics:**
- **Total Days:** 16 (Jan 8-23, 2026)
- **Total Programs:** 39
- **Practice Programs:** 36
- **Mini Projects:** 3
- **Topics Covered:** 13 major topics

### **Breakdown:**
```
Classes & Methods:     16 programs (Days 24-27)
Inheritance:           14 programs (Days 28-32)
Encapsulation:          6 programs (Days 33-34)
Polymorphism:           5 programs (Days 35-36)
Mini Projects:          3 projects (Days 37-39)
```

---

## 🎯 KEY CONCEPTS MASTERED

### **1. Classes & Objects**
- Blueprint vs Instance
- Constructor pattern
- Self parameter
- Instance variables

### **2. Inheritance**
- Code reusability
- Parent-child relationships
- Super keyword
- Multilevel chains
- Method overriding

### **3. Encapsulation**
- Data hiding
- Private variables (__var)
- Protected variables (_var)
- Getter/Setter pattern
- Validation

### **4. Polymorphism**
- Method overriding
- Operator overloading
- Same name, different behavior
- Flexibility

---

## 💡 REAL-WORLD APPLICATIONS

**What I can build now:**
- ✅ Library management systems
- ✅ Banking applications
- ✅ Student record systems
- ✅ E-commerce platforms
- ✅ Inventory management
- ✅ User authentication systems
- ✅ Game character systems
- ✅ Any CRUD application

---

## 📚 LEARNING RESOURCES

**Concepts Practiced:**
- Class design patterns
- Object relationships
- Data modeling
- Security principles
- Business logic implementation
- Error handling

**Skills Developed:**
- Problem decomposition
- Code organization
- Abstraction
- Design thinking
- Real-world modeling

---

## 🔥 WHAT'S NEXT

**After Day 39:**
- Days 40-41: Review & Exam Prep
- Days 42-47: Advanced OOP Projects (Post-exam)
- Module Complete: 50 total programs!

**Then:**
- ✅ Python fundamentals: COMPLETE
- ✅ OOP: COMPLETE
- 🚀 Ready for AI projects (February 1)

---

## ⚡ TIPS FOR SUCCESS

**Best Practices Learned:**
- One class = One responsibility
- Keep methods small and focused
- Use meaningful names
- Validate all inputs
- Handle errors gracefully
- Document your code
- Test as you build

**Common Patterns:**
- Constructor initialization
- Getter/Setter validation
- Parent-child relationships
- Private data with public methods
- Method chaining
- Object composition

---

## 🎓 EXAM-FRIENDLY FEATURES

**Quick Revision Points:**
- Each day has focused topic
- Clear progression of difficulty
- Mini projects for practical application
- Covers all university OOP syllabus
- Interview-ready examples

**For Exams:**
- Review day-wise READMEs
- Focus on mini projects
- Understand concepts, not memorize
- Practice explaining in own words

---

## 📝 NOTES

**Built During:** 5th Semester Exams (Jan 8-25, 2026)  
**Maintained:** Daily GitHub streak  
**Portfolio:** Part of python-learning-journey repo

---

## ✅ MODULE STATUS

**Completion:** 39/39 programs (Days 24-39)  
**Quality:** Production-ready code  
**Documentation:** Complete READMEs  
**Portfolio-Ready:** ✅ Yes

---

**OOP MASTERED! 🎉**  
**Ready for AI Engineering! 🚀**

---

*Last Updated: January 23, 2026*  
*Repository: python-learning-journey/05-oop*  
*Author: Aayush Raj Giri*  
*GitHub: github.com/27raj-giri*
