
# Write a Python program to check if user entered number is ZERO, POSITIVE or
# NEGATIVE until user does not want to quit.
# User will type ‘Quit’ to close the program.

print('Enter input :', end = " ")
while(1) :
    num = input()
    if (num == "Quit") :
        break
    else :
        num = int(num)
        if(num > 0) :
            print(f'{num} is positive')
        elif(num < 0) :
            print(f'{num} is negative')
        else :
            print(f'{num} is zero')


