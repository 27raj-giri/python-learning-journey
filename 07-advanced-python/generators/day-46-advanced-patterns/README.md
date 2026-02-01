# Day 46: Advanced Generator Patterns

Production-ready generator techniques for AI pipelines and data processing.

## 🎯 Concepts

- Custom utility functions
- Generator pipelines (chaining)
- Two-way communication (`.send()`)
- Generator composition
- `yield from` delegation

## 📚 Programs (5)

| # | Program | Concept |
|---|---------|---------|
| 21 | Custom Range | Building stdlib-like functions |
| 22 | Generator Pipeline | Data transformation chain |
| 23 | Generator Send | Interactive generators |
| 24 | Nested Generators | Manual composition |
| 25 | Yield From | Delegation syntax |

## 💡 Key Learning

### Custom Range
```python
def my_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step
```

### Pipeline Pattern (RAG-ready!)
```python
# Process data in stages
source = number_source(10)
filtered = filter_evens(source)
transformed = square_numbers(filtered)

for result in transformed:
    print(result)  # Clean, memory-efficient
```

### Two-Way Communication
```python
gen = interactive_gen()
next(gen)                # Start
gen.send("data")         # Send value into generator
```

### yield from
```python
def main_gen():
    yield from sub_gen()  # Cleaner than manual loop
```

## 🚀 Run
```bash
python 21_custom_range.py
python 22_generator_pipeline.py
python 23_generator_send.py
python 24_nested_generators.py
python 25_yield_from.py
```

## 🎯 AI Applications

✅ **Pipelines** → RAG document processing  
✅ **`.send()`** → Agent state management  
✅ **`yield from`** → Clean async patterns  
✅ **Custom utilities** → Production tools  

---

**Day:** 46 | **Programs:** 5/5 
