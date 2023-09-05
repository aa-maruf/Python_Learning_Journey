# use of max fuction
mx = max (45, 65, 34)
print (mx)

nums= {12,45, 56, 13,} # works in set too
print(max(nums))
print(nums)

# reversed()
numbers = [12, 45, 56, 13]
rev = reversed(numbers)
print(list(rev)) # list Because set is not reversable.set stores in descendin order


# sorted ()
print(sorted(numbers, reverse = True))
players = [
           {'name' : "shakib", "age" : 35},
           {'name' : "Musfiq", "age" : 36},
           {'name' : "Riad", "age" : 37},
           {'name' : "Tamim", "age" : 34},
           {'name' : "Hridoy", "age" : 23}
           ]
sorted_players = sorted (players, key = lambda player : player['age']) # sorting dictionary
print (sorted_players)
