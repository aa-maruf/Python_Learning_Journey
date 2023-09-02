# Reverse a given integer number
# Given:
# 76542

# Expected output:
# 24567

num = input("Enter the number: ")

ans = ""

# for i in range (len(num) -1 , -1, -1) :
#     ans += num[i]

for i in reversed (num) :
    ans += i



ans = int(ans)
print(ans)
    
