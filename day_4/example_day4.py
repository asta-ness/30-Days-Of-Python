multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
string = "I am a teacher and enjoy teaching. I didn't find anything as rewarding as empowering people. " \
         "That is why I created 30 days of python."
print(string)

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t\t5')
print('Day 2\t3\t\t5')
print('Day 3\t3\t\t5')
print('Day 4\t3\t\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')
#New Style String Formating (str.format)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

#Unpacking Characters

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

#String Interpolation / f-Strings
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') # :.2f rodo kiek po kablelio
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#format(): formats string into a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
print('I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country))