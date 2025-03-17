#LEVEL 3
#1.Here we have a person dictionary. Feel free to modify it!
person = {
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


print("Original Person Dictionary:")
print(person)
print()


print("Basic Information:")
print(f"Name: {person['first_name']} {person['last_name']}")
print(f"Age: {person['age']}")
print(f"Country: {person['country']}")
print()


if 'skills' in person:
    print(f"Skills: {', '.join(person['skills'])}")
    print(f"Number of skills: {len(person['skills'])}")
    
   
    if 'Python' in person['skills']:
        print("This person knows Python")
    else:
        print("This person doesn't know Python")
print()


person['skills'].append('SQL')
print(f"Skills after adding SQL: {', '.join(person['skills'])}")
print()


person['address']['city'] = 'Helsinki'
print(f"Updated address: {person['address']}")
print()


person['email'] = 'asabeneh@example.com'
person['phone'] = '+358123456789'
print("Dictionary after adding email and phone:")
print(person)