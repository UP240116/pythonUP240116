#LEVEL 2
#1.Write a code which gives grade to students according to theirs scores:
score = float(input("Enter the student's score: "))
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score"

#2.Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.
mes = input("Introduce un mes: ").lower()
if mes in ["septiembre", "octubre", "noviembre", "september", "october", "november"]:
    estacion = "Autumn"
elif mes in ["diciembre", "enero", "febrero", "december", "january", "february"]:
    estacion = "Winter"
elif mes in ["marzo", "abril", "mayo", "march", "april", "may"]:
    estacion = "Spring"
elif mes in ["junio", "julio", "agosto", "june", "july", "august"]:
    estacion = "Summer"
else:
    estacion = "Mes no válido"
print(f"El mes de {mes} corresponde a la estación: {estacion}") 

#3.The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()


if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    
    fruits.append(new_fruit)
    print("Modified list:", fruits)