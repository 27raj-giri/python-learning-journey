# Day 17 - Recursion Advanced (Interview Level)

**Date:** December 31, 2025  
**Programs:** 8  
**Time:** 6 hours  
**Focus:** Logical recursion, problem-solving, algorithms

## Topics Covered
- Fibonacci pattern (multiple recursive calls)
- Mathematical recursion (GCD, prime)
- Searching in lists
- String manipulation
- Occurrence patterns
- Interview-level thinking

## Programs

### 🟣 Level 4 - Logical Recursion (8 programs)
1. fibonacci_nth.py - Find nth Fibonacci number
2. fibonacci_series.py - Print series up to n
3. is_prime.py - Check prime recursively
4. gcd.py - Find GCD of two numbers
5. count_occurrences.py - Count element in list
6. remove_char.py - Remove all occurrences
7. first_occurrence.py - Find first index
8. last_occurrence.py - Find last index

## Key Learnings
- Break problems into smaller subproblems
- Think recursively, not iteratively
- Multiple recursive calls (Fibonacci)
- Euclidean algorithm (GCD)
- Search patterns in recursion
- **Recursion is thinking, not memorization!**

## Advanced Recursion Pattern
```python
def advanced_recursion(data, target):
    # Base case
    if base_condition:
        return base_value
    
    # Multiple recursive calls or complex logic
    result = combine(
        recursive_call_1(...),
        recursive_call_2(...)
    )
    return result
```
```