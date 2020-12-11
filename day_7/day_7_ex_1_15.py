# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['companyIT','ITcompany'])
print(it_companies)

it_companies.remove('companyIT')
print((it_companies))

A.intersection(B)
print(A)

A.union(B)
print(A)

A.update(B)
print(A)

A.issubset(B)
print(A)


print(A.isdisjoint(B))

del A
del B

age_set = set(age)
print((age_set))

print(len(age))
print(len(age_set))