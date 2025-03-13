age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
st = set(age)
print(len(st))
print(len(age))
#2.Explain the difference between the following data types: string, list, tuple and set
#La diferencia es que los tipo string, es un tipo de variable que nos sirve para almacenar
#caracteres, las listas, para almacenar varios caracteres dentro de una sola variable, los 
#tuple, es de misma forma una lista pero no nos permite modificarla, y los sets
#de misma forma son una manera de almacenar datos, con la diferencia de que estos no nos permiten
#repetir los mismos. 

#3.I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
word = set(sentence.split())
print(len(word))