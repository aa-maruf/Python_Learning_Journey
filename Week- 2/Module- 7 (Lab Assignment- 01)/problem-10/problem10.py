""" 
10. Given a string ‘s’ you need to find the words that are in list ‘a’ and use the next words on string ‘s’ to create a new string. 
Save it inside a file called ‘out.txt’. Remember to close the file after writing.

Write a function named create_new_string() and write your code inside this function.

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

output = "I love visit Bangladesh" (inside a file)

"""

a = ['oh', 'Emelia', 'to']


s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string(s,a):
    words = ""
    for c in s:
        if ((c >= 'A' and c <= 'Z') or (c >= 'a' and  c<= 'z') or c == " "):
            words += c

    s = words.split()
    ans = ""
    for i,word in enumerate(s) :
        if ((word.lower() in a ) or (word.upper() in a) or (word.capitalize() in a)):
            if ans != "":
                ans += " "
            ans += s[i+1]
        
    print(ans)
    with open ("out.txt", 'w') as fileWrite:
        fileWrite.write(ans)
        fileWrite.close()



create_new_string(s,a)

