# Day 15 - Recursion Return-Based

**Date:** December 29, 2025  
**Programs:** 7  
**Time:** 5 hours  
**Focus:** Return values, trusting recursive results

## Topics Covered
- Return statements in recursion
- Building results from recursive calls
- Trusting the recursive call
- Accumulation pattern
- Mathematical recursion

## Programs

### 🟡 Level 2 - Return-Based Recursion (7 programs)
1. sum_1_to_n.py - Sum of first n numbers
2. product_1_to_n.py - Product of first n numbers
3. factorial.py - Calculate factorial
4. sum_of_digits.py - Sum all digits
5. count_digits.py - Count digits in number
6. power_a_b.py - Calculate power a^b
7. max_in_list.py - Find maximum in list

## Key Learnings
- `return x + recursion()` pattern
- Trust the recursive call to solve subproblem
- Combine current value with recursive result
- Base case returns actual value
- Don't fear `return` in recursion!

## Recursion Return Pattern
```python
def recursive_function(n):
    # Base case
    if n == base_condition:
        return base_value
    
    # Recursive case
    return current + recursive_function(n - 1)