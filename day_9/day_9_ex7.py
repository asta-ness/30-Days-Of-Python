person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}
if 'skills' in person:
    skills=person.get('skills')
    number=len(skills)//2
    print(skills[number])

if 'skills' in person:
    skills = person.get('skills')
    exist = 'Python' in skills
    print(exist)

skills = person.get('skills')
javasrcipt_skill = 'JavaScript' in skills
react_skill = 'React' in skills
node_skill = 'Node' in skills
mongodb_skill = 'MongoDB' in skills
python_skill = 'Python' in skills
number=len(skills)

if javasrcipt_skill and react_skill and number ==2:
    print('He is a front end developer')
if node_skill and python_skill and mongodb_skill:
    print('He is a backend developer')
if react_skill and node_skill and mongodb_skill:
    print('He is a fullstack developer')
else:
    print('unknown title')

is_marred = person.get('is_marred')
country = person.get('country')
first_name = person.get('first_name')
last_name = person.get('last_name')
if is_marred == True and country == 'Finland':
    print(first_name, last_name, ' lives in ', country, '. He is marred.')