# Understanding Arrays in Data Structures

Arrays are one of the most fundamental data structures used in programming. They allow storing multiple elements (of the same type) in a contiguous block of memory.



## What is an Array?

An **Array** is a collection of elements stored at contiguous memory locations. The idea is to store multiple items of the same type together.



# Types of Arrays

### 1. **Static Array**

A **Static Array** has a fixed size, which means the number of elements is defined during its creation and cannot be changed later.

#### ✅ Advantages:

* Simple to implement.
* Fast access (O(1) time complexity).
* Less overhead in memory management.

#### ❌ Disadvantages:

* Wasted space if not fully used.
* Cannot grow/shrink dynamically.
* Requires knowing the size in advance.

### 2. **Dynamic Array**

A **Dynamic Array** can grow or shrink in size during runtime. When it runs out of space, it automatically resizes (usually doubles its capacity).

#### ✅ Advantages:

* Flexible in size.
* No need to know final size at creation.
* Automatically manages capacity.

#### ❌ Disadvantages:

* Resizing is expensive (O(n) time occasionally).
* Uses more memory due to extra capacity.



## When to Use

| Use Case                               | Recommended Type     |
| -------------------------------------- | -------------------- |
| Fixed-size, performance-critical logic | Static Array         |
| Unknown or variable size input         | Dynamic Array        |
| Working with built-in types in C/C++   | Static Array         |
| High-level data manipulation (Python)  | Dynamic Array (list) |

---

## Example (Python)

### Static Array:

```python
from array_dataStructure import StaticArray

static_arr = StaticArray(5)
for i in range(5):
    static_arr[i] = i * 10
print("Static array contents:", static_arr)

try:
    static_arr[9] = 5  # This will raise an IndexError
except IndexError as e:
    print("Error:", e)  # Output: Error: Index out of bounds

```

### Dynamic Array:

```python
from array_dataStructure import DynamicArray

dynamic_arr = DynamicArray()
    for i in range(5):
        dynamic_arr.append(i)
    print("Dynamic Array:", dynamic_arr)

```

---

## 📚 Summary

* Arrays are efficient for accessing elements using indices.
* Static arrays are memory-efficient and fast but fixed in size.
* Dynamic arrays are flexible and ideal for situations where the size isn't known in advance.
* Understanding their trade-offs helps in writing better, optimized code.

