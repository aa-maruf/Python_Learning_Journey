""" 
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list, 
then the 1st index item, and so on till the last element. 
any leftover items will get added at the end of the new list

Sample Input:
list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

Sample Output:
['My', 'name', 'is', 'Bond']
 """

list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

list3 = []
for i, j in zip (list1,list2) :
    list3.append(i+j)

if (len(list1) > len(list2)) :
    list3.extend(list1[len(list2) :])  # read append vs extend in hibijibi_notes.md file
elif (len(list1) < len(list2)) :
    list3.extend(list2[len(list1):])

print(list3)
