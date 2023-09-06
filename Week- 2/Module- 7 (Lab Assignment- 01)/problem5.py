""" 
5. You have given a dictionary ‘d’, convert it into a list. The first value will be the key of the dict, and value will come next. 

Example
d = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
output:  [ 'a', 1, 'b',  2, 'c', 3, 'd', 4]


Now do the same for -
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}


Write a function named create_list() and write your code inside this function.
"""
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

def create_list(d):
    ans = []
    for key in d:
        ans.append(key)
        ans.append(d[key])
    print(ans)

create_list(d)