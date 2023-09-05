numbers  = [12, 13, 14, 15, 11, 10]

def getNumbers (nums) :
    for i in nums :
        yield i  # yield is similar to return, but doesn't end the function, conitnues to do rest job.

result = getNumbers(numbers)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print("Hello, Enjoy !")
print(next(result))
print("No fear")
print(next(result))


