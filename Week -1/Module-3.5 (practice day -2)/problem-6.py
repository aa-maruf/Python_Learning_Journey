# Write a program to check if one string contains another. For example, the result will be True if all the characters in the s1 are present in s2, otherwise False. The character’s position doesn’t matter. Take inputs from the user.

# s1 = "Phi"
# s2 = "Phitron"

# Output : True


s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")
ans = True


for char in s1 :
    if char not in s2 :
        ans = False
    
    
if ans :
    print("True")
else :
    print("False")