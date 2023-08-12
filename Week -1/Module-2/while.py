# to stop infinite loop in vs code write ctrl + c
# Learned about how debugging and breakpoint works

num = 0
sum = 0
while num <= 10 :
    num = num + 1
    if num % 2 == 0 :
        continue
    if num > 8 :
       break
    sum = num + sum
    print(num)

print(sum)