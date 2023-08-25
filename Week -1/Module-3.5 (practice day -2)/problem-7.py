# Write a program to check if the given number is a palindrome number.
# Input : 121
# Output : True

num = input("Input: ")
j = len(num) - 1
ans = True

for i in range (int(len(num)/2)) :
    if (num[i] == num[j]) :
        j -= 1
    else :
        ans = False
        break

if ans : 
    print("True")
else :
    print("False")

