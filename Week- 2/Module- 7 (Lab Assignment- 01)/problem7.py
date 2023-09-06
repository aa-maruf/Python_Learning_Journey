""" 
7. Complete the following code (without using the replace function)-

def replace_comma_with_space(text):
    …
    …

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

"""
def replace_comma_with_space(text):
    ans = ""
    for c in text :
        if c == ',':
            ans += " "
        else:
            ans += c
    return ans

s = "I,have,been,practising,python,since,the,course,started"
output = replace_comma_with_space(s)
print(output)