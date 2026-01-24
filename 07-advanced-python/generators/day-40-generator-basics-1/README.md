# Day 40: Generator Basics Part 1

Understanding `yield` and basic generator creation.

## Concepts

- What is `yield`?
- `yield` vs `return`
- Basic generator syntax
- Iterating over generators

## Programs (3)

| # | Program | Concept |
|---|---------|---------|
| 01 | Yield 1-5 | Basic `yield` |
| 02 | Even Numbers | Generator with condition |
| 03 | String Characters | String iteration |

## Key Learning

### What is `yield`?
```python
def simple_gen():
    yield 1  # Pauses here, returns 1
    yield 2  # Resumes, returns 2
    yield 3  # Resumes, returns 3

# Usage
for num in simple_gen():
    print(num)  # 1, 2, 3
```

### `yield` vs `return`
```python
# return - ends function
def with_return():
    return 1
    return 2  # Never executes

# yield - pauses function
def with_yield():
    yield 1
    yield 2  # Executes when resumed
```

## Run
```bash
python 01_yield_1_to_5.py
python 02_even_generator.py
python 03_string_characters.py
```

## Features

✅ Basic `yield` syntax  
✅ Generator iteration  
✅ Conditional generation  
✅ String processing  

---

**Day:** 40/222 | **Programs:** 3/3  
**Next:** Day 41 (Iteration & `next()`)
```
