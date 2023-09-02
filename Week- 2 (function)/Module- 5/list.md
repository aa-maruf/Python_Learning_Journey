<<<<<<< HEAD
This page explains some of the features and methods of various data types in Python, such as lists, tuples, sets, and dictionaries. Here are some examples of each function mentioned in this page:

- **list.append (x)**: This method adds an item x to the end of a list¹[1]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.append("orange")
>>> fruits
['apple', 'banana', 'cherry', 'orange']
```

- **list.extend (iterable)**: This method adds all the items from an iterable (such as another list, a tuple, a set, etc.) to the end of a list²[2]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> vegetables = ["carrot", "celery", "cucumber"]
>>> fruits.extend(vegetables)
>>> fruits
['apple', 'banana', 'cherry', 'carrot', 'celery', 'cucumber']
```

- **list.insert (i, x)**: This method inserts an item x at a given position i in a list³[3]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.insert(1, "orange")
>>> fruits
['apple', 'orange', 'banana', 'cherry']
```

- **list.remove (x)**: This method removes the first item from the list whose value is equal to x⁴[4]⁵[5]. It raises a ValueError if there is no such item⁶[6]⁷[7]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.remove("banana")
>>> fruits
['apple', 'cherry']
```

- **list.pop ([i])**: This method removes the item at the given position i in the list, and returns it⁸[8]. If no index is specified, it removes and returns the last item in the list⁹[9]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.pop()
'cherry'
>>> fruits.pop(0)
'apple'
>>> fruits
['banana']
```

- **list.clear ()**: This method removes all items from the list[^10^][10]. Equivalent to del list [:]¹¹[11]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.clear()
>>> fruits
[]
```

- **list.index (x [, start [, end]])**: This method returns the zero-based index in the list of the first item whose value is equal to x⁵[5]⁴[4]. It raises a ValueError if there is no such item⁶[6]⁷[7]. The optional arguments start and end are used to limit the search to a particular subsequence of the list¹²[12]. For example:

```python
>>> fruits = ["apple", "banana", "cherry", "orange"]
>>> fruits.index("cherry")
2
>>> fruits.index("orange", 2)
3
```

- **list.count (x)**: This method returns the number of times x appears in the list¹³[13]. For example:

```python
>>> fruits = ["apple", "banana", "cherry", "orange", "banana"]
>>> fruits.count("banana")
2
```

- **list.sort (key=None, reverse=False)**: This method sorts the items of the list in place (the arguments can be used for sort customization)¹⁴[14]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers.sort()
>>> numbers
[1, 2, 5, 7, 9]
```

- **list.reverse ()**: This method reverses the elements of the list in place¹⁵[15]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers.reverse()
>>> numbers
[1, 9, 7, 2, 5]
```

- **list.copy ()**: This method returns a shallow copy of the list¹⁶[16]. Equivalent to list [:]¹⁷[17]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers_copy = numbers.copy()
>>> numbers_copy
[5, 2, 7, 9, 1]
```

- **tuple ([iterable])**: This function creates a tuple object from an optional iterable (such as a list, a set, etc.). A tuple is an immutable sequence of values separated by commas¹⁸[18]. For example:

```python
>>> t = tuple([1, 2, 3])
>>> t
(1, 2, 3)
```

- **set ([iterable])**: This function creates a set object from an optional iterable (such as a list, a tuple, etc.). A set is an unordered collection of distinct hashable objects¹⁹[19]. For example:

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

- **dict ([iterable])**: This function creates a dictionary object from an optional iterable (such as a list of key-value pairs, a tuple of key-value pairs, etc.). A dictionary is an unordered collection of key-value pairs, where the keys are immutable and unique. For example:

```python
>>> d = dict([("name", "Alice"), ("age", 25)])
>>> d
{'name': 'Alice', 'age': 25}
```

- **enumerate (iterable, start=0)**: This function returns an enumerate object that yields pairs of indexes and values from an iterable (such as a list, a tuple, etc.). The optional argument start specifies the starting index. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> list(enumerate(fruits))
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

- **zip (*iterables)**: This function returns a zip object that yields tuples of corresponding elements from one or more iterables (such as lists, tuples, sets, etc.). For example:

```python
>>> numbers = [1, 2, 3]
>>> letters = ["a", "b", "c"]
>>> list(zip(numbers, letters))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

- **reversed (sequence)**: This function returns a reversed object that yields the elements of a sequence (such as a list, a tuple, etc.) in reverse order. For example:

```python
>>> numbers = [1, 2, 3]
>>> list(reversed(numbers))
[3, 2, 1]
```

- **sorted (iterable, *, key=None, reverse=False)**: This function returns a new sorted list from the items in an iterable (such as a list, a tuple, a set, etc.). The optional arguments key and reverse can be used for sort customization. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> sorted(fruits)
['apple', 'banana', 'cherry']
>>> sorted(fruits, reverse=True)
['cherry', 'banana', 'apple']
```



Source: Conversation with Bing AI😊, 8/29/2023
=======
This page explains some of the features and methods of various data types in Python, such as lists, tuples, sets, and dictionaries. Here are some examples of each function mentioned in this page:

- **list.append (x)**: This method adds an item x to the end of a list¹[1]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.append("orange")
>>> fruits
['apple', 'banana', 'cherry', 'orange']
```

- **list.extend (iterable)**: This method adds all the items from an iterable (such as another list, a tuple, a set, etc.) to the end of a list²[2]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> vegetables = ["carrot", "celery", "cucumber"]
>>> fruits.extend(vegetables)
>>> fruits
['apple', 'banana', 'cherry', 'carrot', 'celery', 'cucumber']
```

- **list.insert (i, x)**: This method inserts an item x at a given position i in a list³[3]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.insert(1, "orange")
>>> fruits
['apple', 'orange', 'banana', 'cherry']
```

- **list.remove (x)**: This method removes the first item from the list whose value is equal to x⁴[4]⁵[5]. It raises a ValueError if there is no such item⁶[6]⁷[7]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.remove("banana")
>>> fruits
['apple', 'cherry']
```

- **list.pop ([i])**: This method removes the item at the given position i in the list, and returns it⁸[8]. If no index is specified, it removes and returns the last item in the list⁹[9]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.pop()
'cherry'
>>> fruits.pop(0)
'apple'
>>> fruits
['banana']
```

- **list.clear ()**: This method removes all items from the list[^10^][10]. Equivalent to del list [:]¹¹[11]. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits.clear()
>>> fruits
[]
```

- **list.index (x [, start [, end]])**: This method returns the zero-based index in the list of the first item whose value is equal to x⁵[5]⁴[4]. It raises a ValueError if there is no such item⁶[6]⁷[7]. The optional arguments start and end are used to limit the search to a particular subsequence of the list¹²[12]. For example:

```python
>>> fruits = ["apple", "banana", "cherry", "orange"]
>>> fruits.index("cherry")
2
>>> fruits.index("orange", 2)
3
```

- **list.count (x)**: This method returns the number of times x appears in the list¹³[13]. For example:

```python
>>> fruits = ["apple", "banana", "cherry", "orange", "banana"]
>>> fruits.count("banana")
2
```

- **list.sort (key=None, reverse=False)**: This method sorts the items of the list in place (the arguments can be used for sort customization)¹⁴[14]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers.sort()
>>> numbers
[1, 2, 5, 7, 9]
```

- **list.reverse ()**: This method reverses the elements of the list in place¹⁵[15]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers.reverse()
>>> numbers
[1, 9, 7, 2, 5]
```

- **list.copy ()**: This method returns a shallow copy of the list¹⁶[16]. Equivalent to list [:]¹⁷[17]. For example:

```python
>>> numbers = [5, 2, 7, 9, 1]
>>> numbers_copy = numbers.copy()
>>> numbers_copy
[5, 2, 7, 9, 1]
```

- **tuple ([iterable])**: This function creates a tuple object from an optional iterable (such as a list, a set, etc.). A tuple is an immutable sequence of values separated by commas¹⁸[18]. For example:

```python
>>> t = tuple([1, 2, 3])
>>> t
(1, 2, 3)
```

- **set ([iterable])**: This function creates a set object from an optional iterable (such as a list, a tuple, etc.). A set is an unordered collection of distinct hashable objects¹⁹[19]. For example:

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

- **dict ([iterable])**: This function creates a dictionary object from an optional iterable (such as a list of key-value pairs, a tuple of key-value pairs, etc.). A dictionary is an unordered collection of key-value pairs, where the keys are immutable and unique. For example:

```python
>>> d = dict([("name", "Alice"), ("age", 25)])
>>> d
{'name': 'Alice', 'age': 25}
```

- **enumerate (iterable, start=0)**: This function returns an enumerate object that yields pairs of indexes and values from an iterable (such as a list, a tuple, etc.). The optional argument start specifies the starting index. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> list(enumerate(fruits))
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

- **zip (*iterables)**: This function returns a zip object that yields tuples of corresponding elements from one or more iterables (such as lists, tuples, sets, etc.). For example:

```python
>>> numbers = [1, 2, 3]
>>> letters = ["a", "b", "c"]
>>> list(zip(numbers, letters))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

- **reversed (sequence)**: This function returns a reversed object that yields the elements of a sequence (such as a list, a tuple, etc.) in reverse order. For example:

```python
>>> numbers = [1, 2, 3]
>>> list(reversed(numbers))
[3, 2, 1]
```

- **sorted (iterable, *, key=None, reverse=False)**: This function returns a new sorted list from the items in an iterable (such as a list, a tuple, a set, etc.). The optional arguments key and reverse can be used for sort customization. For example:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> sorted(fruits)
['apple', 'banana', 'cherry']
>>> sorted(fruits, reverse=True)
['cherry', 'banana', 'apple']
```



Source: Conversation with Bing AI😊, 8/29/2023
>>>>>>> 0a46fafe3e33e8165022587f09beec2b2ef318e1
