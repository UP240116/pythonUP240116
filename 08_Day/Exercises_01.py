#1.Create an empty dictionary called dog
dog = {}

#2.Add name, color, breed, legs, age to the dog dictionary
dog={'name':'Max', 'color':'Brown', 'breed':'Labrador','legs': '4', 'age':'3'}
print("Diccionario dog:", dog)
#3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Juan',
    'last_name': 'Pérez',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'México',
    'city': 'Ciudad de México',
    'address': 'Calle Principal 123'
}
print("\nDiccionario student:", student)
#4.Get the length of the student dictionary
skills = student['skills']
skills_type = type(skills)
print("\nValor de skills:", skills)
print("Tipo de datos de skills:", skills_type)

#5.Get the value of skills and check the data type, it should be a list
student['skills'].append('HTML')
student['skills'].append('CSS')
print("\nSkills después de modificar:", student['skills'])

#6.Modify the skills values by adding one or two skills
keys = list(student.keys())
print("\nClaves del diccionario student:", keys)

#7.Modify the skills values by adding one or two skills
values = list(student.values())
print("\nValores del diccionario student:", values)

#8.Get the dictionary values as a list
items = list(student.items())
print("\nDiccionario student como lista de tuplas:")
for item in items:
    print(item)

#9.Change the dictionary to a list of tuples using items() method
del student['marital_status']
print("\nDiccionario student después de eliminar 'marital_status':", student)

#10.Delete one of the items in the dictionary
del dog
print("\nEl diccionario 'dog' ha sido eliminado.")

#11.Delete one of the dictionaries
del student
print("El diccionario 'student' todavía existe:", student)