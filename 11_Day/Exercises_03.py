#LEVEL 3
#1.Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:  
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  
print(is_prime(10))  
print(is_prime(13))

#2.Write a functions which checks if all items are unique in the list.
def all_items_unique(lst):
    return len(lst) == len(set(lst))  
print(all_items_unique([1, 2, 3, 4]))  
print(all_items_unique([1, 2, 3, 3])) 

#3.Write a function which checks if all the items of the list are of the same data type.
def all_items_same_type(lst):
    if len(lst) < 2:  
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print(all_items_same_type([1, 2, 3, 6]))  
print(all_items_same_type([1, "two", 3])) 

#4.Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_python_variable(var):
    if var.isidentifier() and not keyword.iskeyword(var):
        return True
    return False
print(is_valid_python_variable("valid_var")) 
print(is_valid_python_variable("123invalid"))  
print(is_valid_python_variable("class"))

#5.Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

from collections import Counter
from countries_data import countries_d 

# 1. Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Function to check if all items are unique in a list
def all_items_unique(lst):
    return len(lst) == len(set(lst))

# 3. Function to check if all items of the list are of the same data type
def all_items_same_type(lst):
    if len(lst) < 2:  # A list with 0 or 1 item always has the same type
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

# 4. Function to check if a provided variable is a valid Python variable
def is_valid_python_variable(var):
    if var.isidentifier() and not keyword.iskeyword(var):
        return True
    return False

# 5. Function to get the most spoken languages in the world (from a data file)
def most_spoken_languages_in_the_world(n=10):
    language_count = {}
    
    # Count occurrences of each language
    for country in countries:
        language = country["language"]
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    # Sort languages by count in descending order
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return top n languages
    return sorted_languages[:n]

# 6. Function to get the most populated countries (from a data file)
def most_populated_countries(n=10):
    # Sort countries by population in descending order
    sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
    
    # Return top n populated countries
    return sorted_countries[:n]