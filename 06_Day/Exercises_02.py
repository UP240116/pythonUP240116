#LEVEL 2
# 1. Unpack siblings and parents from family_members
# First 6 elements are siblings, last 2 are parents

hermanos = "family_members" [:6]  # type: ignore # Los primeros 6 elementos son hermanos
padres = "family_member"[6:]    # Los últimos 2 elementos son padres
print(f"Hermanos: {hermanos}")
print(f"Padres: {padres}")

# 2. Create and join fruit, vegetables and animal products tuples
fruits = ('apple', 'banana', 'orange', 'mango')
vegetables = ('carrot', 'potato', 'broccoli')
animal_products = ('milk', 'cheese', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item(s)
# For odd number of items
middle_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle_index]
# For even number of items
middle_items = food_stuff_tp[len(food_stuff_tp)//2-1:len(food_stuff_tp)//2+1]

# 5. Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# 7. Check if items exist in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # Output: False
print('Iceland' in nordic_countries)  # Output: True
