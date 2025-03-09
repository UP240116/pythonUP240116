#1.Declare an empty list
empty_list = list()

#2.Declare a list with more than 5 items
lst = ['5', '6', '7', '8', '9']

#3.Find the length of your list
print(len(lst))

#4.Get the first item, the middle item and the last item of the list
print(lst[0])
print(lst[3])
print(lst[4])

#5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Sebastián', '19', '1.75', 'Married', 'Villas de Nuestra Señora de la Asunción']
print(mixed_data_types)

#6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7.Print the list using _print()_
print(it_companies)

#8.Print the number of companies in the list
print(len(it_companies))

#9.Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#10.Print the list after modifying one of the companies
it_companies[0] = 'FACEBOOK'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.insert(1, 'Arduino')
print(it_companies)

#12.Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Youtube')
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3]= 'AMAZON'
print(it_companies)

#14.Join the it_companies with a string '#;  '
it_str= '#; '.join(it_companies)
print(it_str)

#15.Check if a certain company exists in the it_companies list.
print('AMAZON' in it_companies)

#16.Sort the list using sort() method
print(sorted(it_companies))

#17.Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18.Slice out the first 3 companies from the list
del it_companies [0:2]
print(it_companies)

#19.Slice out the last 3 companies from the list
del it_companies [4:6]
print(it_companies)

#20.Slice out the middle IT company or companies from the list
del it_companies [1]
print(it_companies)

#21.Remove the first IT company from the list
del it_companies[0]
print(it_companies)

#22.Remove the middle IT company or companies from the list
del it_companies[0]
print(it_companies)

#23.Remove the last IT company from the list
del it_companies[1]
print(it_companies)

#24.Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25.Destroy the IT companies list
del it_companies

#26.Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
end = front_end + back_end
print(end)

#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
Full_Stack = end.copy()
Full_Stack.insert(5, 'Python')
Full_Stack.insert(5, 'SQL')
print(Full_Stack)