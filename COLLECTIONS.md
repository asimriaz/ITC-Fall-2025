

##  **1. LIST**

* **Ordered** (keeps items in the same sequence)
* **Changeable (mutable)** → you can add, remove, modify items
* **Allows duplicates**
* Written with **[ ]**

### Example:

```python
my_list = [10, 20, 30, 20]
my_list[1] = 99       # modification allowed
```



##  **2. TUPLE**

* **Ordered**
* **Not changeable (immutable)** → cannot modify after creation
* **Allows duplicates**
* Written with **( )**

### Example:

```python
my_tuple = (10, 20, 30)
# my_tuple[1] = 99  ❌ ERROR: cannot modify
```

Tuples are **faster** than lists and often used for fixed data.



##  **3. DICTIONARY**

* **Key–Value pairs**
* **Unordered (Python 3.7+ keeps insertion order, but still accessed by key)**
* **Keys must be unique**
* Mutable (you can add/modify/delete)
* Written with **{ key: value }**

### Example:

```python
my_dict = {"name": "Asim", "age": 25}
my_dict["age"] = 26     # modify value
my_dict["city"] = "Lahore"  # add new key
```



##  **4. SET**

* **Unordered**
* **No duplicate values**
* Mutable (you can add/remove)
* Written with **{ }**, but **empty set must use set()**

### Example:

```python
my_set = {10, 20, 30, 20}
print(my_set)   # {10, 20, 30} → duplicates removed
```

Used for mathematical operations like **union**, **intersection**, etc.



#  Summary Table

| Type      | Ordered | Mutable | Allows Duplicates     | Syntax         |
| --------- | ------- | ------- | --------------------- | -------------- |
| **List**  | Yes     | Yes     | Yes                   | `[ ]`          |
| **Tuple** | Yes     | No      | Yes                   | `( )`          |
| **Dict**  | Yes*    | Yes     | Keys: No, Values: Yes | `{key: value}` |
| **Set**   | No      | Yes     | No                    | `{ }`          |

*Dictionaries maintain insertion order but are accessed by key, not index.


