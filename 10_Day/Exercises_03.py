#LEVEL 3
#1.Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries 
countries_with_land = [country for country in countries if 'land' in country.lower()]
print(countries_with_land)

#2.This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)
#3.Go to the data folder and use the countries_data.py file.
from collections import Counter
from countries_data import countries_d 

#3.1.What are the total number of languages in the data
language_counter = Counter()
unique_languages = set()

for country in countries_d:
    for language in country["languages"]:
        language_counter[language] += 1
        unique_languages.add(language)


total_languages = len(unique_languages)

#3.2.Find the ten most spoken languages from the data
most_spoken_languages = language_counter.most_common(10)

most_populated_countries = sorted(
    countries_d, key=lambda x: x["population"], reverse=True
)[:10]

#3.3.Find the 10 most populated countries in the world
top_10_populated = [(country["name"], country["population"]) for country in most_populated_countries]
print(f"Total number of unique languages: {total_languages}")
print("\nTen most spoken languages:")
for lang, count in most_spoken_languages:
    print(f"{lang}: {count} countries")

print("\nTen most populated countries:")
for country, population in top_10_populated:
    print(f"{country}: {population}")