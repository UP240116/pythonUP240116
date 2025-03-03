#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
cadena1 = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(cadena1)

#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
cadena2 = 'Coding '+ 'For ' + 'Lom ' + 'All '
print(cadena2)

#3.Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#4.Print the variable company using print().
print(company)

#5.Print the length of the company string using len() method and print().
print(len(company))

#6.Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7.Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9.Cut(slice) out the first word of Coding For All string.
First_word = company [7:14]
print(First_word)

#10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
company3 = 'Coding For All'
print(company3.find('coding'))

#11.Replace the word coding in the string 'Coding For All' to Python.
print(company3.replace('coding ', 'python '))

#12.Change Python for Everyone to Python for All using the replace method or other methods.
company4 = 'Python for Everyone'
print(company4.replace('Everyone', 'all'))

#13.Split the string 'Coding For All' using space as the separator (split()) .
company5 = 'Coding For All'
print(company5.split(' '))

#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_empresas = empresas.split(', ')
print(lista_empresas)

#15.