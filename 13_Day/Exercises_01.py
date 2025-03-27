#1.Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 10]

print(filtered_numbers)

#2.Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_1 = [num for sublist in list_of_lists for inner_list in sublist for num in inner_list]
print("Method 1 (List Comprehension):", flattened_1)

import itertools
flattened_2 = list(itertools.chain.from_iterable(itertools.chain.from_iterable(list_of_lists)))
print("Method 2 (itertools):", flattened_2)

flattened_3 = []
for sublist in list_of_lists:
    for inner_list in sublist:
        flattened_3.extend(inner_list)
print("Method 3 (Nested loops):", flattened_3)

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flattened_4 = flatten(list_of_lists)
print("Method 4 (Recursive):", flattened_4)

#3.Using list comprehension create the following list of tuples:
result = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(result)

#4.Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [
    [country[0].upper(), country[0][:3].upper(), capital.upper()] 
    for sublist in countries 
    for country, capital in sublist
]

print(flattened_countries)

#5.Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dict = [
    {'country': country[0].upper(), 'city': capital.upper()} 
    for sublist in countries 
    for country, capital in sublist
]

print(countries_dict)

#6.Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(concatenated_names)

#7.Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_calc = lambda points, calc_type: (
    (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if calc_type == 'slope' 
    else points[0][1] - ((points[1][1] - points[0][1]) / (points[1][0] - points[0][0])) * points[0][0] if calc_type == 'intercept'
    else None
)

point1 = (0, 0)
point2 = (5, 7)
slope = linear_calc([(point1), (point2)], 'slope')
print(f"Slope: {slope}")

y_intercept = linear_calc([(point1), (point2)], 'intercept')
print(f"Y-intercept: {y_intercept}")

