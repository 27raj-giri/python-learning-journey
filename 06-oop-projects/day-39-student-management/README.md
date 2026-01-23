# Day 39: Student Management System

Inheritance and polymorphism with a 3-level class hierarchy.

## 🎯 Concepts

- **Inheritance:** Person → Student → GraduateStudent
- **Polymorphism:** Method overriding (`display_info()`)
- **`super()`:** Parent class access

## 🏗️ Structure
```
Person (base)
  └─ Student
      └─ GraduateStudent
School (manages all)
```

## 📁 Files

- `student_system.py` - Classes
- `main.py` - Interactive
- `demo.py` - Auto demo

## 🚀 Run
```bash
python demo.py
python main.py
```

## 💡 Key Code
```python
# Polymorphism in action
school = School("Tech Institute")
school.add_student(Student("Raj", 20, "UG001", "Junior"))
school.add_student(GraduateStudent("Aayush", 21, "GRAD001", 
                   "Masters", "AI Research", "Dr. Sharma"))

school.display_all_students()  # Calls correct display_info() for each!
```

## 📊 Features

✅ 3-level inheritance  
✅ Method overriding  
✅ Polymorphic behavior  
✅ `super()` usage  

---

**Day:** 39 | **OOP Projects:** 3/3 ✅  
**Next:** Generators (Day 40)
```