# Day 16 - Recursion with Arrays & Strings

**Date:** December 30, 2025  
**Programs:** 8  
**Time:** 5 hours  
**Focus:** List/string recursion, index-based patterns

## Topics Covered
- Passing lists to recursive functions
- Index-based recursion
- String manipulation recursively
- Checking properties with recursion
- Building strings from recursion

## Programs

### 🟠 Level 3 - Arrays & Strings (8 programs)
1. print_list.py - Print all list elements
2. print_list_reverse.py - Print list in reverse
3. sum_list.py - Sum of list elements
4. min_in_list.py - Find minimum
5. is_sorted.py - Check if sorted
6. count_vowels.py - Count vowels in string
7. reverse_string.py - Reverse string recursively
8. is_palindrome.py - Check palindrome

## Key Learnings
- List slicing in recursion: `lst[1:]`
- Index-based vs slicing approach
- String building with recursion
- Boolean return for checking
- Trust recursion with data structures!

## List Recursion Pattern
```python
def process_list(lst, index=0):
    # Base case
    if index == len(lst):
        return base_value
    
    # Process current element
    current = lst[index]
    
    # Combine with recursive result
    return combine(current, process_list(lst, index+1))
```
```