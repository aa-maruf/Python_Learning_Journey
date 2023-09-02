numbers  = [12, 13, 14, 15, 11, 10]
numbers_iter = iter(numbers)
try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("No problem")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("Take rest. Do something else now.")
    print(next(numbers_iter))
    print(next(numbers_iter)) # This line will go to except.
except:
    print("Iteration is stopped")
