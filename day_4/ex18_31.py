company_name = 'Coding For All'
#ex18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
# using list comprehension (mawe)
#str1 = "senior health inFormation development"
#print acronym1  # S.H.I.D  note that join() does not add the final period

print( '.'.join([word[0].upper() for word in company_name.split()]))

#ex19 Create an acronym or an abbreviation for the name 'Coding For All'.

string_1 = 'Coding For All'
print( '.'.join([word[0].upper() for word in string_1.split()]))

#ex20-21 Use index to determine the position of the first occurrence of C/F in Coding For All.

print(string_1.index('C'))
print(string_1.index('F'))

#ex22
print(string_1.rfind('i'))

#ex23 -24
sentence_23 = 'You cannot end a sentence with because because because is a conjunction'
word_1 ='because'
print(sentence_23.index(word_1))
print(sentence_23.rindex(word_1))

#ex25
print(sentence_23[31:55])

#ex28-29
print(company_name.startswith('Coding'))
print(company_name.endswith('Coding'))

#ex30
sentence_30=' Coding For All '
print(sentence_30.strip(' '))