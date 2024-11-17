# Python Club - Day 2 Lesson Plan

## 1. String Deep Dive (25 minutes)
### String Methods Review
* **Accessing Characters**
   * String indexing (positive and negative indices)
   * Example: `text[0]`, `text[-1]`
* **Essential String Methods:**
   * `len()` - Get string length
   * `.upper()`, `.lower()`, `.title()`, `.capitalize()`
   * `.strip()` - Remove whitespace
   * `.replace(old, new)` - Replace text
   * `.startswith()`, `.endswith()`
   * `.count()` - Count occurrences
   * `.isdigit()`, `.isalpha()`, `.isalnum()`
* **String Slicing**
   * Basic syntax: `[start:end:step]`
   * Examples:
     * `text[2:5]` - Characters from index 2 to 4
     * `text[:5]` - Start to index 4
     * `text[5:]` - Index 5 to end
     * `text[::2]` - Every second character
     * `text[::-1]` - Reverse string

## 2. Lists Deep Dive (30 minutes)
### List Basics
* **Creating Lists**
   * Empty list: `[]` or `list()`
   * List with items: `[1, 2, 3]`
   * Mixed data types: `[1, "hello", True, 3.14]`
   * Nested lists: `[[1, 2], [3, 4]]`

### List Operations
* **Accessing Elements**
   * Indexing: `list[0]`
   * Negative indexing: `list[-1]`
   * Slicing: `list[1:4]`

### List Methods
* **Adding Elements**
   * `.append(item)` - Add to end
   * `.extend(iterable)` - Add multiple items
* **Removing Elements**
   * `.remove(item)` - Remove by value
   * `.pop(index)` - Remove by index
   * `.clear()` - Remove all items
* **Ordering**
   * `.sort()` - Sort in place
   * `.reverse()` - Reverse in place
* **Other Operations**
   * `.count(item)` - Count occurrences
   * `len(list)` - Get length

## 3. Loops (30 minutes)
### For Loops
* **Basic Syntax:**
   ```python
   for item in sequence:
       # code block
   ```
* **Common Use Cases:**
   * `range(start, stop, step)`
   * Looping through lists
   * Looping through strings
* **Example Patterns:**
   ```python
   # Count from 0 to 9
   for i in range(10):
       print(i)
   
   # Loop through list
   for item in my_list:
       print(item)
   ```

### While Loops
* **Basic Syntax:**
   ```python
   while condition:
       # code block
   ```
* **Control Statements:**
   * `break` - Exit loop
   * `continue` - Skip to next iteration
   * `pass` - Do nothing
* **Common Patterns:**
   * Counter loops
   * Input validation
   * Game loops

# IF TIME PERMITS (OPTIONAL)
## 4. Dictionaries (20 minutes if time permits)
### Dictionary Basics
* **Creating Dictionaries:**
   * Empty: `{}` or `dict()`
   * With items: `{"key": "value"}`
* **Operations:**
   * Access: `dict["key"]`
   * Add/Update: `dict["key"] = value`
   * Delete: `del dict["key"]`

### Dictionary Methods
* **Common Methods:**
   * `.get(key, default)` - Safe access
   * `.keys()` - Get all keys
   * `.values()` - Get all values
   * `.items()` - Get key-value pairs
   * `.update()` - Merge dictionaries
   * `.pop(key)` - Remove and return value
   * `.clear()` - Remove all items
