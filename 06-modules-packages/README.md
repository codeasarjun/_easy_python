## What is a Python Module?

A **module** in Python is a single file containing Python code. It can define functions, classes, and variables. Modules help in organizing code into manageable sections.

### Example of a Module

We have a file named `math_module.py` with the following content:

```python

def add(a, b):
    return a + b
```
We can use it by - 
```python
import math_module # importing the module

result = math_module.add(10, 5) # calling funtions
print(f"The sum is: {result}")
```

## What is a Python Package?

A package is a collection of modules organized in directories. It allows you to group related modules together. A package directory must contain a special file named __init__.py (which can be empty) to be recognized as a package.

### Example of a Package

We have a file named `test_package.py` with the following content:

```python
test_package/
    __init__.py
    module1.py
    module2.py
```


