#ex32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

#ex33

line='''I am enjoying this challenge.
I just wonder what is next.'''
print(line)
print('I am enjoying this challenge.\nI just wonder what is next.')

# ex34
print('Name\t\tAge\t\tCountry')
print('Asabeneh\t250\t\tFinland')

#ex35
radius = 10
area = 3.14 * radius ** 2
formated_string= 'The area of a cricle with radius %d is %2d' %(radius, area) + ' ' + 'meters square.'
print(formated_string)

#ex36

a=8
b=6
print('{}+{}={}'.format(a, b, a+b))
print('{}+{}={}'.format(a, b, a-b))
print('{}+{}={}'.format(a, b, a*b))
print('{}+{}={}'.format(a, b, a/b))
print('{}+{}={}'.format(a, b, a%b))
print('{}+{}={}'.format(a, b, a//b))
print('{}+{}={}'.format(a, b, a**b))