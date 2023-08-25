""" Write a program to display all prime numbers within a range. You will be given two integers l and r . You have to print all the prime numbers present in the given range l and r.
Input : 25 50

Output :
29
31
37
41
43
47
 """

l, r  = input("Enter the range: ").split()
l = int(l)
r = int(r)

prime = True

for i in range (l, r) :
    prime = True
    for j in range (2,int( i/2 + 1)) :
        if (i % j == 0) :
            prime = False
            break
    if prime :
        print(i)

