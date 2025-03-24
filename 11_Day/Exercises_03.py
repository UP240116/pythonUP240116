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
from countries_data import countries 

#  --------------------------------------------------------
def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#  ------------------------------------------------------
def all_items_unique(lst):
    return len(lst) == len(set(lst))

# ------------------------------------------------------
def all_items_same_type(lst):
    if len(lst) < 2:  
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

# -------------------------------------------------
def is_valid_python_variable(var):
    if var.isidentifier() and not keyword.iskeyword(var):
        return True
    return False

#  --------------------------------------------
def most_spoken_languages_in_the_world(n=10):
    language_count = {}
    
    
    for country in countries:
        language = country["language"]
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

   
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
  
    return sorted_languages[:n]

#------------------------------------------
def most_populated_countries(n=10):
   
    sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
    
   
    return sorted_countries[:n]