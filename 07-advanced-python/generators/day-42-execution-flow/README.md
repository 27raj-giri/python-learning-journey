# Day 42: Generator Execution Flow

Understanding pause-resume behavior and when code actually runs.

## 🎯 Concepts

- Pause-resume mechanism
- `yield` execution points
- Generator state management
- Before/after yield behavior

## 📚 Programs (3)

| # | Program | Concept |
|---|---------|---------|
| 08 | Before/After Yield | Code around `yield` |
| 09 | Predict Output | Understanding flow |
| 10 | Execution Control | When code runs |

## 💡 Key Learning

### Execution Flow
```python
def demo():
    print("Before yield 1")
    yield 1
    print("Before yield 2")
    yield 2
    print("After all yields")

gen = demo()            # Nothing printed yet!
print(next(gen))        # Prints "Before yield 1", yields 1
print(next(gen))        # Prints "Before yield 2", yields 2
# next(gen)             # Prints "After all yields", StopIteration
```

### Key Points
- Generator doesn't run until `next()` is called
- Pauses at `yield`, resumes on next `next()`
- Code after `yield` runs on next iteration

## 🚀 Run
```bash
python 08_before_after_yield.py
python 09_predict_output.py
python 10_execution_control.py
```

## 📊 Features

✅ Pause-resume understanding  
✅ Execution timing control  
✅ Generator state awareness  
✅ Flow prediction skills  

---

**Day:** 42 | **Programs:** 3/3  
**Next:** Day 43 (Logic & Conditions)
