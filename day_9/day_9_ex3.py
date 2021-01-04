number_one = input('Enter number one: ')
number_two = input('Enter number two: ')
number_one = int(number_one)
number_two = int(number_two)
if number_one > number_two:
    print(number_one, 'is greater than' , number_two)
else:
    print(str(number_one) + ' is smaller than ' + str(number_two))