def add (num1, num2) :
    print(num1,num2)

print("Add function output: ")
add (num2 = 200, num1 = 100)    # set parameter value by this

# Optional constructor
def mul (num1, num2 = 1) :
    print (num1 * num2)
print("mul function output: ")
mul (12)


# Multiple variable as parameter
def product(*numbers) :   #args
    add = int(1)
    for num in numbers :
        add*= num
    return add
print("product function output: ")
print(product (10, 20 ,30))

add = int(0)
def show (num1, num2, *numbers) :
    print(num1, num2)
    print(numbers)
print("show function output: ")
show(10, 20, 30,40, 50)



