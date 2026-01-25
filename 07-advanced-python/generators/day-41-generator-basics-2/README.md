# Day 41: Generator Basics Part 2

Generator iteration and manual control with `next()`.

## 🎯 Concepts

- Parameterized generators
- List to generator conversion
- Generator execution flow
- Manual iteration with `next()`

## 📚 Programs (4)

| # | Program | Concept |
|---|---------|---------|
| 04 | Natural Numbers | Generator with parameter |
| 05 | Squares Conversion | List → Generator |
| 06 | Execution Flow | Understanding pause-resume |
| 07 | Manual next() | Controlling iteration |

## 💡 Key Learning

### Using `next()`
```python
def count():
    yield 1
    yield 2
    yield 3

gen = count()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)       # StopIteration error
```

### List vs Generator
```python
# List - stores all in memory
squares_list = [i*i for i in range(1000000)]  # Heavy!

# Generator - computes on demand
squares_gen = (i*i for i in range(1000000))   # Light!
```

## 🚀 Run
```bash
python 04_natural_numbers.py
python 05_squares_conversion.py
python 06_execution_flow.py
python 07_manual_next.py
```

## 📊 Features

✅ Parameterized generators  
✅ Generator expressions  
✅ Manual `next()` control  
✅ Execution flow understanding  

---

**Day:** 41 | **Programs:** 4/4  
**Next:** Day 42 (Execution Flow Deep Dive)
```
