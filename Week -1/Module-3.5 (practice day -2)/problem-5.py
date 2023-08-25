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







