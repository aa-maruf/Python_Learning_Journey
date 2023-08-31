numbers = [ 0, 1, 2 ,3 ,4 , 5]

print (numbers[1])
print (numbers[-4])
print (numbers[3 :])
print (numbers [1 : 4])
print (numbers [0 : 5 : 2])   #start : end : steps
print (numbers [5 : 0 : -2])   #start : end : steps
print (numbers[ : ])
print (numbers[ : : -1])


# list append function
numbers.append(int(6))
print (numbers[ : ])

# list extend function
roll = [ 110, 111, 112]
numbers.extend(roll)
print(numbers[ : ])

# insert function with try except
numbers.insert(7, 7)
print(numbers[ : ])

try :
    numbers.remove("Nothing.. this will return valueError !")
except: 
    print("ValueError")
else :
    print(numbers[ : ])


# list pop function
numbers.pop()
numbers.pop(-2)
numbers.pop(len(numbers) -1 )
print(numbers[ : ])


# list clear() clears the list. numbers.clear()

# list index function
idx = numbers.index(int(7))
print(f'Index = {idx}')

# list count - > number of times x appears in the list
cnt = numbers.count("banana")
print(f'count = {cnt}')

# list reverse
numbers.reverse()
print(numbers[ : ])

# list sort function
numbers.sort()
print(numbers[ : ])

# list copy function 
numbers_copy = numbers.copy()
print(f'copy : {numbers_copy[ : ]}')



