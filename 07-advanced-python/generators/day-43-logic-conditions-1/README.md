# Day 43: Generators with Logic Part 1

Applying conditions and filters inside generators.

## 🎯 Concepts

- Conditional `yield`
- Filtering data with generators
- Logic inside generators
- Practical filtering patterns

## 📚 Programs (3)

| # | Program | Concept |
|---|---------|---------|
| 11 | Positive Numbers | Filter with condition |
| 12 | Divisible by 3 & 5 | Multiple conditions |
| 13 | Vowels Generator | String filtering |

## 💡 Key Learning

### Conditional Yield
```python
def positive_only(numbers):
    for num in numbers:
        if num > 0:
            yield num  # Only yield if condition met

# Usage
nums = [-2, 5, -1, 8, 0, 3]
for n in positive_only(nums):
    print(n)  # 5, 8, 3
```

### Multiple Conditions
```python
def divisible_3_and_5(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield i
```

## 🚀 Run
```bash
python 11_positive_numbers.py
python 12_divisible_3_5.py
python 13_vowels_generator.py
```

## 📊 Features

✅ Conditional generation  
✅ Data filtering  
✅ Multiple condition checks  
✅ Practical use cases  

---

**Day:** 43 | **Programs:** 3/3  
**Next:** Day 44 (Advanced Logic)
