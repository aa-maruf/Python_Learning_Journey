my_list = ["@F1", "OBCD", '!', "@f2","ADDAB", '!',"@F3","OKKA", '!']

# EXPECTED : {"@F1": "OBCD", "@f2":"ADDAB","@F3":"OKKA" } # CONVERT TO DICTIONARY

my_dict = {}
n = len (my_list)

for i,val in enumerate(my_list) :
    if i > n:
        break
    if val[0] == '@':
        my_dict[val] = my_list[i + 1]
    
    i += 3

print(my_dict)

