your_fruits = input('Enter your fruits: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
if your_fruits in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(your_fruits)
    print(fruits)