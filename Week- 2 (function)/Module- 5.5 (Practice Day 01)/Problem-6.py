""" 
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary
Hints: Search about Dictionary Comprehension

Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected Output:
{'name': 'Kelly', 'salary': 8000}
 """

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

ans_dict = {(key,value) for key,value in sample_dict.items() if key not in keys}
# new_dict = {k: sample_dict[k] for k in keys}  more easier way 
print(ans_dict)
