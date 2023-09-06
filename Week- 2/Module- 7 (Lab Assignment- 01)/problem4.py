""" 
4. Fix this code, get help from google. Copy the error message and search on web.
def print_hi():
    print("hi")

print(print_hi()) # you can't change this lin 

"""
# Reason Behind error: print() function prints hi and returns NONE that is also being printed by outer print function.
# So output :
#  hi 
# NONE
# Here is the fixed code.
def print_hi():
    _print = "hi"
    return _print

print(print_hi()) # you can't change this lin 
