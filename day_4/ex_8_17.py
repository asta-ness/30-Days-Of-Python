#ex9-10
company_name = 'Coding For All'
print(company_name.strip('Coding '))
print(company_name[7:])
#ex 11
print(company_name.find('Coding'))
print(company_name.index('Coding'))
#ex 12 Change Python for Everyone to Python for All using the replace method or other methods.
print(company_name.replace('Coding', 'Python'))
#ex13 Split the string 'Coding For All' using space as the separator (split())
print(company_name.split())
#ex14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
media ='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(media.split(', '))
print(media.split())
#ex15 What is the character at index 0 in the string Coding For All.
print(company_name[0])
#ex16 the last character
print(company_name[-1])
#ex17
print(company_name[10])