#LEVEL 2
#1.Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    evens = 0
    odds = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
            
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))

#1.1.Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))

#1.2.Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if not value:
        return True
    return False
print(is_empty([])) 
print(is_empty([1, 2, 3]))  
print(is_empty("")) 
print(is_empty("Hello"))  

#1.3.Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
from collections import Counter
import math

def evens_and_odds(n):
    evens = 0
    odds = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
            
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_empty(value):
    if not value:
        return True
    return False


def calculate_mean(lst):
    if len(lst) == 0:
        return "List is empty"
    return sum(lst) / len(lst)


def calculate_median(lst):
    if len(lst) == 0:
        return "List is empty"
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]


def calculate_mode(lst):
    if len(lst) == 0:
        return "List is empty"
    count = Counter(lst)
    mode_data = count.most_common(1)
    return mode_data[0][0]


def calculate_range(lst):
    if len(lst) == 0:
        return "List is empty"
    return max(lst) - min(lst)


def calculate_variance(lst):
    if len(lst) == 0:
        return "List is empty"
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def calculate_std(lst):
    if len(lst) == 0:
        return "List is empty"
    variance = calculate_variance(lst)
    return math.sqrt(variance)

numbers = [1, 2, 3, 4, 5]

print(calculate_mean(numbers))    
print(calculate_median(numbers))
print(calculate_mode(numbers))    
print(calculate_range(numbers)) 
print(calculate_variance(numbers)) 
print(calculate_std(numbers))    