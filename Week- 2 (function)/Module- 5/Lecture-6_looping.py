numbers = [12, 45, 65, 23, 89]

# addition using built in 
total = sum(numbers) # built in function
print(total)

# addition using loop
sum = 0
for i in numbers:
    sum += i

print(sum)

# for index use enumerate
for i,num in enumerate(numbers) :
    print(i, num)       # This could be done using simply num and where num gives a pair consists of both index & numbers
    


# addition using set
sum = 0
nums = {12, 45, 65, 23, 89}
for i in numbers:
    sum += i

print(sum)

tuples = 12, 45, 65, 23, 89 # tuples of same procces ei addition possible

# addition in dictionary
sum = 0
marks = {'physics' : 12, 'chemistry' : 45, 'math' : 56}
for key in marks :
    val = marks[key] # key stores the key name so marks[key] = value
    sum += val
    print(key, val)
print(f'sum : {sum}')

for subject,mark in marks.items(): # eksathe key & value duitai store hbe
    print(subject, mark)







