""" Display Fibonacci series up to 10 terms

0  1  1  2  3  5  8  13  21  34
 """



a = int(0)
b = int (1)

#print (a,b)
for i in range (10) :
    print (a, end = " ")
    c = a + b
    # print(type(c))
    a = b 
    b = c
