#LEVEL 1
#1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

#2.Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    import math
    area = math.pi * r * r
    return area

#3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            return f"Error: '{arg}' is not a number. All arguments must be numbers."
    
    return total

#4.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(7))

#5.Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

#6.Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
   
    if x1 == x2:
        return float('inf')  
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 2, 3, 6))

#7.Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    import math
    
   
    discriminant = b**2 - 4*a*c
    
    
    if a == 0:
        if b == 0:
            return "Not a valid equation" if c != 0 else "Infinite solutions"
        else:
            return [-c/b]  

    if discriminant > 0:
  
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]
    elif discriminant == 0:
     
        x = -b / (2*a)
        return [x]
    else:
 
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return [complex(real_part, imaginary_part), complex(real_part, -imaginary_part)]

print(solve_quadratic_eqn(1, -3, 2))

#8.Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
my_list = [1, 2, 3, 4, 5]
print_list(my_list)

#9.Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

#10.Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_list = []
    for item in lst:
        if isinstance(item, str):
            capitalized_list.append(item.capitalize())
        else:
            capitalized_list.append(item)  
    return capitalized_list
print(capitalize_list_items(['apple', 'banana', 'cherry']))
print(capitalize_list_items(['python', 'javascript', 123, 'html']))

#11.Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    new_list = lst.copy()  
    new_list.append(item)  
    return new_list

#12.Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    return [element for element in lst if element != item]

#13.Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return sum(range(1, n + 1))
print(sum_of_numbers(5))

#14.Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(1, n+1, 2):  # Start from 1, step by 2 to get only odd numbers
        total += i
    return total
result = sum_of_odds(10)
print(result)

#15.Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    total = 0
    for i in range(2, n+1, 2):  
        total += i
    return total
print(sum_of_even(20))