#day 5 ex 1-26
#ex1
empty_list =[]
print(len(empty_list))

#ex2
animals = ['suo', 'kate', 'vezlys', 'papuga', 'triusis', 'ziurke']
#ex3
print(len(animals))
#ex4
print(animals[0], animals[2], animals[-1])

#5
mixed_data_types = ['Asta', 51, 164, 'Oslo']
print(mixed_data_types)

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#ex7
print(it_companies)

#ex8
print(len(it_companies))

#ex9
a = len(it_companies)
b = a // 2
print(b)
print(it_companies[0], it_companies[b], it_companies[-1])

#ex10
it_companies[2] = 'microsoft'
print(it_companies)

#ex11
it_companies.append('Cosac')
print(it_companies)

#ex12
it_companies.insert(2, 'astapasta')
print(it_companies)

#ex13
a = it_companies[1].upper()
print(a)

#ex14
it_companies.extend(['#;  '])
print(it_companies)

#ex15 does't work with another ex.
# it_companies = set(it_companies)
# if 'certain' in it_companies:
#     print('Element Exists')
# else:
#     print('Element NOT Exists')

#ex16
it_companies.sort()
print(it_companies)

#ex17
it_companies.reverse()
print(it_companies)

#ex18
print(it_companies[2:])

#ex19
print(it_companies[:-2])

#ex20
#print(it_companies[0:2, 4:-1])

#ex21
print(it_companies.pop(0))

#ex22
print(it_companies.pop(-1))

#ex23
del it_companies[-1]
print(it_companies)

#ex24
# del it_companies
# print(it_companies)
#
# #ex25
# it_companies.clear()
# print(it_companies)

#ex26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

#ex27
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)