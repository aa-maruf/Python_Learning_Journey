""" 
# comprehension decreases readability. 
# It is not recommended to use.
 """

numbers  = [12, 13, 14, 15, 11, 10]
odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)

# this can be easily done using comprehesion

odd_numbers2 = [num for num in numbers if num%2 == 1 if num % 5 != 0]
# here for loop is in the middle, if condition is at the end and the append is doing by num at the beginnign of comprehesion.
print(odd_numbers2)

# another example:
names = ['Shakib','Jamal', 'Sana','Baki']
ages = [35, 34, 32, 36]
pairs = [(name, age) for name in names for age in ages if age > 35] 
print(pairs)
 
# This comprehension works like this - 
# for name in names :
#     for age in ages:
#         if age > 35 :
#             print(name, age, end = "\n")

