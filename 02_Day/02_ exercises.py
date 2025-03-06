num_one = 5
num_two = 4

Total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print('Total:',num_one + num_two)
print('Diff:',num_two - num_one)
print('Producto:',num_two * num_one)
print('Division:',num_one / num_two)
print('Remainder:',num_one % num_two)
print('Exp:',num_one ** num_two)
print('Floor_Division:',num_one // num_two)

radius = 30
area_of_circle = 3.1416 * radius **2
print('El area es:',area_of_circle) 
circum_of_circle = 3.1416 * radius
print('La circunferencia es:',circum_of_circle)

import math
radius = float(input("Introduce el radio del círculo: "))
area = math.pi * radius ** 2
print(f"El área del círculo es: {area:.2f}")


primer_nombre = input("Introduce tu primer nombre: ")
apellido = input("Introduce tu apellido: ")
pais = input("Introduce tu país: ")
edad = input("Introduce tu edad: ")

print(f"Hola, {primer_nombre} {apellido} de {pais}. Tienes {edad} años.")


help('keywords')