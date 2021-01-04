age = input('Enter your age: ')
my_age = 30
age = int(age)
year = my_age - age
if year > age:
    year = str(year)
    print('You are ' + year + ' years older than me')
else:
    year = str(-year)
    print ('You are ' + year + ' years youger than me')