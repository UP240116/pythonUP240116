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

#15.What character is at index 10 in "Coding For All" string.
print(company5[0])

#16.What is the last index of the string Coding For All.
print(len(company5) - 1) 

#17.What character is at index 10 in "Coding For All" string.
print(company5[10])

#18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(''.join(word[0].upper() for word in 'Python For Everyone'.split()))

#19.Create an acronym or an abbreviation for the name 'Coding For All'.
print(''.join(word[0].upper() for word in 'Coding For All'.split()))

#20.Use index to determine the position of the first occurrence of C in Coding For All.
print(company5.index('C'))

#21.Use index to determine the position of the first occurrence of F in Coding For All.
print(company5.index('F'))

#22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company5.rfind('l'))

#23.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24.Use rindex to find the position of the last occurrence of the word because in the following sentence:
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

#25.Slice out the phrase 'because because because' in the following sentence: 
print('You cannot end a sentence with because because because is a conjunction'.rindex('because because because'))

#26.Find the position of the first occurrence of the word 'because' in the following sentence:
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

#27.Slice out the phrase 'because because because' in the following sentence: 
print('You cannot end a sentence with because because because is a conjunction'. rindex('because because because'))

#28.Does ''Coding For All' start with a substring Coding?
print(company5.startswith('coding'))

#29. Does 'Coding For All' end with a substring coding?
print(company5.endswith('coding'))

#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
company6 = '   Coding For All      '.strip ()
print(company6)

#31.Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'. isidentifier)
print('thirty_days_of_python'. isidentifier())

#32.The following list contains the names of some of python libraries:
company7 =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(company7))

#33.Use the new line escape sequence to separate the following sentences
print('I am enjoying this challenge.')