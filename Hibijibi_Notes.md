Modules = header files
dictionary = map c++
keyword = not , as, if, pass, None, from, try, return, True, yield etc 
Packages = Don't know how to explain. For using it installing pip is required
":" =  slicing operator
'**' = power operator 

type(num)
x,y = input().split()
if char is not in s2 :

sleep(2) from time import sleep
import datetime as dt

abs()
a = math.ceil() math.floor()  import math / from math import sin, ceil  -> a - ceil(x)
sum(numbers)  / from function import add   result = add(420, 30)
n = len(num)
new_str = str.lower()
ord(c) ASCII     chr(ord(c)) char
count()   list.count(x)
difference_update set1.difference_update(set2) eliminates set2 element from set1

reversed for i in reversed(numbers) :
zip for i,j in zip (list1, list2) :
enumerate (for index)  for i,num in enumerate(numbers) :

global x
list.append() set.add
f = lambda x: x*2 
num = map(f, numbers)


appned vs extend: 
```python
 # append 
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list) # [1, 2, 3, 4]

    my_list.append([5, 6])
    print(my_list) # [1, 2, 3, 4, [5, 6]] <-
```

```python
    # extend 
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list) # [1, 2, 3, 4, 5] <-

```