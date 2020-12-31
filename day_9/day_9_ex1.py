age = input('Enter your age: ')
a = 18
if int(age) < 18:
    a = a - int(age)
    a = str(a)
    print('You need ' +  a + ' more years to learn to drive.')
else:
    print ('You are old enough to learn to drive.')
