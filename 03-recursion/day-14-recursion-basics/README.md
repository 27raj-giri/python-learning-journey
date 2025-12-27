# Day 14 - Recursion Basics

**Date:** December 28, 2025  
**Programs:** 7  
**Time:** 4 hours  
**Focus:** Print-based recursion, base cases, simple calls

## Topics Covered
- Base case and recursive case
- Print inside recursion
- Countdown and count-up patterns
- No return confusion
- Building confidence with recursion

## Programs

### 🟢 Level 1 - Absolute Basics (7 programs)
1. print_1_to_n.py - Count up from 1 to n
2. print_n_to_1.py - Count down from n to 1
3. print_even_n_to_1.py - Even numbers descending
4. print_odd_1_to_n.py - Odd numbers ascending
5. print_n_natural.py - First n natural numbers
6. countdown_n_to_0.py - Countdown to zero
7. print_hello_n_times.py - Print string n times

## Key Learnings
- Every recursion needs a base case
- Call the function inside itself
- Print-based recursion is easiest to understand
- No return needed for print-only recursion
- Trust the recursive call!

## Recursion Pattern
```python
def recursive_function(n):
    # Base case
    if n == 0:
        return
    
    # Recursive case
    recursive_function(n - 1)
    print(n)  # Print after or before call
```
```