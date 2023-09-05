<<<<<<< HEAD
""" 
tuple 
# similar to set 
# doesn't require bracket also can be done with 1st bracket
# immutable - can't be changed
# so, we can't change tuple, but if there are mutable items like list, set inside tuple
# then we can change it, because list is mutable. 
 """

numbers_tuple = 12, 13 , 14 
print(numbers_tuple)
nums_tuple = (100, 101, 102)
print(nums_tuple) # using 1st bracket


tuple2d = ([12, 45, 12], [45, 11, ])
tuple2d[0][1] = 99  # we can change [1] because it is inside a list.
# but changing tuple2d[0] fully is not possible 
# so tuple2d[0] is a tuple but tuple2d[0][1] is a list

print(tuple2d)
=======
""" 
tuple 
# similar to set 
# doesn't require bracket also can be done with 1st bracket
# immutable - can't be changed
# so, we can't change tuple, but if there are mutable items like list, set inside tuple
# then we can change it, because list is mutable. 
 """

numbers_tuple = 12, 13 , 14 
print(numbers_tuple)
nums_tuple = (100, 101, 102)
print(nums_tuple) # using 1st bracket


tuple2d = ([12, 45, 12], [45, 11, ])
tuple2d[0][1] = 99  # we can change [1] because it is inside a list.
# but changing tuple2d[0] fully is not possible 
# so tuple2d[0] is a tuple but tuple2d[0][1] is a list

print(tuple2d)
>>>>>>> 0a46fafe3e33e8165022587f09beec2b2ef318e1
