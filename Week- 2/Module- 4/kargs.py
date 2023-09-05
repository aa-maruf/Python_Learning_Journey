def full_name (f_name, l_name) :
    name = f' {f_name} {l_name}'
    return name
name = full_name(l_name ='Looser', f_name= 'Maruf')
print(name)


def family(You, **other_details) :
    print(You, other_details)

family (You = "Maruf" , Age = 22, University = 'AUST', Subject = 'CSE', Semester = 2.2)

def all_types (first, *args, **kargs) :
    print(first)
    for word in args:
        print(word)
    for key,value in kargs.items() :
        print (key,value)

all_types("Maruf", "Learning", "Code", Language = "Python", source = "Phitron")

