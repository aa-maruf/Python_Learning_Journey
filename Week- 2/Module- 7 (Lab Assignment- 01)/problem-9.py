""" 9. You need to make a positive story into a negative by changing some of its words automatically.
 Someone gave you a list `replace with’ and 
 asked to find the words that are in that list in string ‘s’ and replace them with the next word of that list.

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


Output example (one done for you): 
"I am the thief of Baghdad..........."

Write a function named replace_word() and write your code inside this function.


 """

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

def replace_word(s,replace_with):
    s = s.split(" ")
    ans = ""

    for i,val in enumerate(s):
        if i > 0 :
            ans += " "
        if val in replace_with:
            ans += replace_with[replace_with.index(val) + 1]
        else :
            ans += val

    print(ans)

replace_word(s,replace_with)


# Easy Solution -
# for i in range(0, len(replace_with), 2):
#     s = s.replace(replace_with[i], replace_with[i+1])

# print(s)
     