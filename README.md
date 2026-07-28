# String Helper Module

A Python module that provides utility functions for common string manipulation tasks. This project demonstrates modular programming in Python by organizing reusable string operations into a separate module.

## Features

The module includes the following functions:

### `change_case(orig_string: str)`

Returns a new string where:
- Uppercase letters become lowercase.
- Lowercase letters become uppercase.

**Example**

```python
from string_helper import change_case

print(change_case("Hello World"))
```

**Output**

```
hELLO wORLD
```

---

### `split_in_half(orig_string: str)`

Splits a string into two halves and returns them as a tuple.

If the string contains an odd number of characters, the first half is shorter.

**Example**

```python
from string_helper import split_in_half

print(split_in_half("Python"))
```

**Output**

```
('Pyt', 'hon')
```

---

### `remove_special_characters(orig_string: str)`

Removes all special characters from a string while preserving:
- Uppercase letters
- Lowercase letters
- Numbers
- Spaces

**Example**

```python
from string_helper import remove_special_characters

print(remove_special_characters("Hello@2026! #Python"))
```

**Output**

```
Hello2026 Python
```

---

## Project Structure

```
.
├── string_helper.py    # Module containing helper functions
├── main.py             # Example usage (optional)
└── README.md
```

---

## Concepts Practiced

- Python Modules
- Function Design
- String Manipulation
- Conditional Logic
- Character Validation
- Code Reusability

---

## Requirements

- Python 3.10 or later

---

## Learning Objective

This project was created as part of my Python learning journey to understand how modules help organize reusable code and improve program structure.

---

## Future Improvements

- Add unit tests using `unittest` or `pytest`
- Include type validation
- Add more string utility functions
- Publish as a reusable Python package

---

## Author

**Anish Gutti**

GitHub: https://github.com/Anish-185