""" 
Write a program to create function calculation() such that 
it can accept two variables and calculate addition and subtraction. 
Also, it must return both addition and subtraction in a single return call. 
Receive the returned values and print the type. 
HInts: Please google how to return multiple values from a function in python

 """
def calculation(a, b) :
    return a+b, a-b

result = calculation(10,5)
print(result)
print(type(result))

 