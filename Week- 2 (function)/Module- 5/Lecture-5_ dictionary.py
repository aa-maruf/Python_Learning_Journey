
marks = {'physics' : 12, 'chemistry' : 45, 'math' : 56}
marks['math'] = 56.5
marks['english'] = 89
del marks['chemistry']
print(marks)

# stroing keys
marks_keys = marks.keys()
marks_values = marks.values()
marks_items = marks.items() # pair eksathe
print(f'{marks_keys}\n {marks_values}\n {marks_items}')

marks.clear()

print(marks)