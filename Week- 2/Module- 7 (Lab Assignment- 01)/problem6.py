""" 
6. Complete the following code
def clean_string(text):
    ....
    ....
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)


If you face any errors, fix them. Get help from google. Do not ask others.
"""

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
def clean_string(text):
    output = ""
    for c in text:
        if c >= 'A' and c <= 'Z' or c >='a' and c <='z':
            output += c
        
    return output


output = clean_string(s)
print(output)
