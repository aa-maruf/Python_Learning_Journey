""" Count all uppercase, lowercase, digits, and special symbols from a given
"P@#yn26at^&i5ve"
Total counts of chars, digits, and symbols 

Uppercase = 1
Lowercase = 7 
Digits = 3 
Symbol = 4
 """

take = input("Give input : ")
upper = int (0)
lower = int (0)
digits = int (0)
symbol = int (0)

for c in take :
    if (c >= 'a' and c <= 'z') :
        lower+=1 
    elif (c >= 'A' and c <= 'Z') :
        upper += 1
    elif (c >= '0' and c <= '9') :
        digits += 1
    else :
        symbol += 1

print (f'Uppercase = {upper}' )
print (f'Lowercase = {lower}')
print (f'Digits = {digits}')
print (f'Symbol = {symbol}')