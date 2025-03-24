# Python List Cheat Sheet

## 1. Advanced List Methods
```python
# Extend a list
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)  # [1, 2, 3, 4, 5, 6]

# Count occurrences
nums = [1, 2, 2, 3, 2, 4]
nums.count(2)  # Output: 3

# Find index of an element
nums.index(3)  # Output: 2

# Sort a list
nums.sort()  # Sorts in ascending order
nums.sort(reverse=True)  # Sorts in descending order

# Reverse a list
nums.reverse()

# Copy a list
copied = nums.copy()
```

## 2. Deep Copy vs. Shallow Copy
```python
import copy

# Shallow Copy (nested lists still linked)
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99  # Modifies original too

# Deep Copy (independent copy)
deep = copy.deepcopy(original)
deep[0][0] = 100  # Original remains unchanged
```

## 3. List Comprehension Tricks
```python
# Generate squares
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested loops (Cartesian product)
pairs = [(x, y) for x in range(2) for y in range(2)]  # [(0,0), (0,1), (1,0), (1,1)]

# Flatten nested lists
nested = [[1, 2], [3, 4]]
flat = [num for sublist in nested for num in sublist]  # [1, 2, 3, 4]

# Dictionary & Set Comprehension
squares_dict = {x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}
unique_squares = {x**2 for x in [-1, 1, -2, 2]}  # {1, 4}
```

## 4. Multi-Dimensional Lists
```python
# 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
matrix[1][2]  # Output: 6

# Iterate through a 2D list
for row in matrix:
    for item in row:
        print(item, end=" ")  # 1 2 3 4 5 6 7 8 9

# Create a 3x3 grid of zeros
grid = [[0] * 3 for _ in range(3)]
```

## 5. Efficiency & Performance of List Operations

| Operation           | Complexity |
|---------------------|------------|
| `lst[i]` (Indexing) | O(1) |
| `lst.append(x)` | O(1) (Amortized) |
| `lst.insert(i, x)` | O(n) |
| `del lst[i]` | O(n) |
| `for x in lst` (Iteration) | O(n) |
| `lst.sort()` | O(n log n) |
| `lst.reverse()` | O(n) |

```python
# Append is faster than insert
nums = list(range(1000000))

import time
start = time.time()
nums.append(5)  # O(1)
print("Append Time:", time.time() - start)

start = time.time()
nums.insert(0, 5)  # O(n)
print("Insert Time:", time.time() - start)
```

**Use `sorted()` when you need a new list:**  
```python
nums = [3, 1, 4]
sorted_nums = sorted(nums)  # Returns a new list
nums.sort()  # Modifies in-place
```

**Use `deque` for fast insert/remove at the start:**  
```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # O(1)
dq.popleft()      # O(1)
```

