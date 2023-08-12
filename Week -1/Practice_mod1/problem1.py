# Suppose you have a floating number N.1 then,
# Floor is the greatest integer less than or equal to N. And Ceil is the smallest
# number greater than or equal to N.
# Example: for 3.4 Floor is 3 and Ceil if 4.

# Write a python program that takes a floating number from users using input() and
# outputs both Floor and Ceil of that number.



import math

num = float(input('Enter a floating number: '))
Floor = math.floor(num)
Ceil = math.ceil(num)

print(f'The floor of {num} is {Floor} and the ceil of {num} is {Ceil}')
