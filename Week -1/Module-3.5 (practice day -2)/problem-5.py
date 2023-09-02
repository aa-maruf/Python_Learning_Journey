""" Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"

Output : AzbycX """



s1 = input("enter first string : ")
s2 = input("enter second string: ")
reverse1 = ""
reverse2 = ""
for c in reversed(s1) :
    reverse1 += c
for c in reversed(s2) :
    reverse2 += c
# if (len(s1) < len(s2)) :
#     x = s1
#     s1 = reverse
#     reverse = x

i = int(len(s1)) - 1
j = int(len(s2)) - 1
print(i,j)
s3 = ""

while i >= 0 or j >= 0 : 
    if ( i >= 0) :
        s3 += reverse1[i]
        i -= 1
    if ( j >= 0) :
        s3 += s2[j]
        j -= 1


print(s3)


# s1 = "Abc"
# s2 = "Xyz"
# s3 = ""
# for i in range(min(len(s1), len(s2))):
#     s3 += s1[i] + s2[-i-1]
# if len(s1) > len(s2):
#     s3 += s1[len(s2):]
# elif len(s2) > len(s1):
#     s3 += s2[len(s1):]
# print(s3)







