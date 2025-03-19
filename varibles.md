# 📚 Variables in Python: Complete Summary

---

## 🧠 What is a Variable?

✅ A **variable** is a name that stores data or a value in memory.  
✅ It acts as a container that holds data, which can be accessed and modified later.

---

## 🎯 How Variables Work

- You assign a value to a variable using the `=` (assignment) operator.
- The variable name points to the value stored in memory.

### 📝 Syntax:
```python
variable_name = value
```

### 🔥 Example:
```python
# Assigning values to variables
x = 5          # Integer
y = 3.14       # Float
name = "John"  # String

# Print variable values
print(x)       # Output: 5
print(y)       # Output: 3.14
print(name)    # Output: John
```

---

## 📝 Types of Variables in Python

Python is **dynamically typed**, meaning you don’t need to specify the type of a variable. It automatically detects the type.

### 🎯 Common Data Types:
| Data Type    | Example                | Description               |
|--------------|-----------------------|---------------------------|
| `int`        | `x = 10`               | Integer numbers           |
| `float`      | `y = 3.14`             | Decimal numbers           |
| `str`        | `name = "Alice"`       | Text/String values        |
| `bool`       | `is_active = True`     | Boolean (True/False)      |
| `list`       | `numbers = [1, 2, 3]`  | List of items             |
| `tuple`      | `point = (3, 4)`       | Immutable collection      |
| `dict`       | `person = {"name": "John", "age": 25}` | Key-value pairs |
| `set`        | `fruits = {"apple", "banana"}` | Unordered unique items |

---

## 🔥 Reassigning Variables

You can change the value of a variable anytime by reassigning it.
```python
x = 10
print(x)    # Output: 10

x = "Hello"
print(x)    # Output: Hello
```
👉 The same variable `x` first stores an **integer** and later a **string**.

---

## ⚡ Multiple Assignments

You can assign multiple variables in one line.
```python
a, b, c = 1, 2.5, "Python"
print(a, b, c)  # Output: 1 2.5 Python
```

---

## 🚫 Rules for Naming Variables

1. ✅ **Start with a letter or underscore:** `name`, `_value`  
2. ✅ **Use letters, numbers, and underscores:** `user_age`, `x1`  
3. ❌ **Cannot start with a number:** `1name` → Invalid  
4. ❌ **No special characters allowed:** `user@name` → Invalid  
5. ✅ **Case-sensitive:** `name` and `Name` are different.  

---

## 🔍 Best Practices for Naming Variables

✅ Use descriptive names:
```python
age = 25
student_name = "Alice"
total_price = 99.99
```
❌ Avoid single letters for complex programs:
```python
a = 25   # Not descriptive
```

