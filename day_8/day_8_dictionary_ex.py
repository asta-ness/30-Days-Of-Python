empty_dict_dog ={}
dict_dog ={
    'name': 'Mopsis',
    'Color': 'Black',
    'breed':'terjer',
    'legs':'short'
}
dict_student= {
    'first_name':'Petras',
    'last_name':'Petraitis',
    'gender':'male',
    'age':'30',
    'marital_status':True,
    'skills':['Word','Excel','PowerPoint'],
    'country':'Norway',
    'city':'Bergen',
    'address':'Langata 15'
}

print(len(dict_student))
print(type(dict_student.get('skills')))

dict_student['skills'].append('Paint')
print(dict_student)

keys = dict_student.keys()
print(keys)

values = dict_student.values()
print(values)

print(dict_student.items())

del dict_student['city']

print(dict_student)

del dict_dog

print(dict_dog)

