"""
 1. Create a string out of some words given in a list -

l = ["This", "is", "very", "fantastic"]


Expected Output:
"This is very fantastic"

Write a function named create_string() and write your code inside this function.

"""

def create_string(str) :
    ans = ""
    for i,val in enumerate(str):
        if (i > 0):
            ans += " "
        ans += val
    return ans

l = ["This", "is", "very", "fantastic"]
print(create_string(l))