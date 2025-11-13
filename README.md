[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s-vEZwzq)
# Python Exercises: String Manipulation

## Overview
Implement two functions in `string_utils.py` to practice string manipulation.

### Problem 1: Split at First Digit
Write `split_at_digit(formula)` to split a string into:
1. **Prefix**: The part before the first digit.
2. **Number**: The first digit onward as an integer.  
If no digits exist, return the original string and `1`.

**Examples**:  
`split_at_digit("H22")` → `("H", 22)`  
`split_at_digit("NaCl")` → `("NaCl", 1)`  

---

### Problem 2: Split Before Each Uppercase
Write `split_before_each_uppercase(formula)` to split a string before every uppercase letter. Keep the uppercase letters in the result.

**Examples**:  
`split_before_each_uppercase("NaCl")` → `["Na", "Cl"]`  
`split_before_each_uppercase("C6H12O6")` → `["C6", "H12", "O6"]`  

---

### Instructions
1. Implement both functions in `string_utils.py`.
2. Test with examples and edge cases provided in the `.ipynb` files.
3. Submit (by commit) the completed file.
