# clean the data and get a string output 'a e i o u'

data = "aNtEriOur\n\t>>"

new_data = data.lower()

output_data = ""

n = len(output_data)
i = 0

for c in new_data :
    if (c == 'a'  or c == 'e' or c == 'i'  or c == 'o' or c == 'u') :
        if (i > 0) :
            output_data += " "
        output_data += c
    i += 1


print (output_data)