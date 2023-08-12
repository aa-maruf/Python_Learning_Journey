# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.(don’t use any python built in function)
# Example :  pHitrOn.iO presents "Python COuRSe".
# Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE”

take = input("give the input: ")
ans = ""
for c in take :
    if c >= 'a' and c <= 'z' :
        ans += chr(ord(c) - 32)
    elif c >= 'A' and c <= 'Z' :
        ans += chr(ord(c) + 32)
    else :
        ans += c

print (ans)