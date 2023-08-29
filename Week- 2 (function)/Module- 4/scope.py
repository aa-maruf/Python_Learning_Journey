""" 
global variable ki?
global variable ke function er vitore value set kra jabe na.
seta kra jonno global keyword use krte hbe
conceptual class. 
Link : https://phitron.io/ph891/video/ph891-4-4-access-and-modify-global-variables

 """


balance = 100

def calculate (price , quantity):
    cost = price * quantity
    balance = cost
    return balance


print(f'Global : {balance}' )
print(calculate(5, 10))


def calculate2 (price , quantity):
    global balance    # used global keyword
    cost = price * quantity
    balance = balance - cost
    return balance

print(f'Before : {balance}' )
print(calculate2(5, 10))
print(f'After : {balance}' )


