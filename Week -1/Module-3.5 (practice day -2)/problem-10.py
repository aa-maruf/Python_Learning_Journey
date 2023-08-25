# Write a program to print the following star pattern using the for loop
# Input : 5
# Output :
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

num = int (input("input: "))

for i in range (num + 1) :
    j = i
    while(j)  :
        print ("*",end=" ")
        j -= 1
    print("\n")


for j in range (num - 1 ,0,-1) :
    while(j)  :
        print ("*",end=" ")
        j -= 1
    print("\n")