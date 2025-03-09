# 1. Create an empty tuple
empty_tuple = ()
# Alternative way
empty_tuple = tuple()

# 2. Create tuples containing names of sisters and brothers
sisters = ('Maria', 'tr', 'Sophia')
brothers = ('James', 'Michael', 'David')

# 3. Join brothers and sisters tuples and assign to siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print(f"I have {num_siblings} siblings.")  # Output: I have 6 siblings.

# 5. Modify siblings tuple and add parents
# Since tuples are immutable, we need to create a new tuple
parents = ('Sergio', 'Bertha')
family_members = siblings + parents
print(family_members)