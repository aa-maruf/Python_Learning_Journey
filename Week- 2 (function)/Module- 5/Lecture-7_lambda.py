<<<<<<< HEAD
""" 
# lambda function [similar concept like cpp lambda]
# python map [c++ map stl and python map is not same :O]
# c++ stl map is similar to dictionary!
# python map works like sort or for_each function 
# where comparator or lambda function can be inserted.
# it is also same. provide the comparator function and the array.
# it will call the function for each element of array
 """

def square(x) :
    return x*x

result = square(6)
print(result)

# Using Lambda

square_lambda = lambda x : x*x
result = square_lambda(6)
print(result)

add = lambda x,y : x+y
sum = add(45, 56)
print(sum)


# Use of python map and lambda function
numbers = [12, 11, 10, 9 , 50]
double_it = lambda x : x * 2
doubled_num = map(double_it, numbers)
doubled_num2 = map(lambda x : x* 2, numbers)

print(f'numbers: {numbers}\ndoubled_num : {list(doubled_num)}\ndoubled_num2 : {list(doubled_num2)}')


bigger_numbers = filter(lambda num : num< 50, numbers)
print(numbers)
print (list(bigger_numbers))

players = [
    {'name' : 'shakib' , 'age':35},
    {'name' : 'Musfiq' , 'age':36},
    {'name' : 'Tamim' , 'age':34} 
    ]

senior_players = filter (lambda players : players ['age'] >=35, players)
print(list(senior_players))
=======
""" 
# lambda function [similar concept like cpp lambda]
# python map [c++ map stl and python map is not same :O]
# c++ stl map is similar to dictionary!
# python map works like sort or for_each function 
# where comparator or lambda function can be inserted.
# it is also same. provide the comparator function and the array.
# it will call the function for each element of array
 """

def square(x) :
    return x*x

result = square(6)
print(result)

# Using Lambda

square_lambda = lambda x : x*x
result = square_lambda(6)
print(result)

add = lambda x,y : x+y
sum = add(45, 56)
print(sum)


# Use of python map and lambda function
numbers = [12, 11, 10, 9]
double_it = lambda x : x * 2

doubled_num = map(double_it, numbers)
doubled_num2 = map(lambda x : x* 2, numbers)

print(f'numbers: {numbers}\ndoubled_num : {list(doubled_num)}\ndoubled_num2 : {list(doubled_num2)}')

>>>>>>> 0a46fafe3e33e8165022587f09beec2b2ef318e1
