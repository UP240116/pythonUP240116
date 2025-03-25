#LEVEL 3
#1.Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(input_list):

    shuffled_list = input_list.copy()
    
   
    random.shuffle(shuffled_list)
    
    return shuffled_list

example_list = [1, 2, 3, 4, 5]
print("Original list:", example_list)
print("Shuffled list:", shuffle_list(example_list))

#2.Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random
def generate_unique_random_numbers():
     return random.sample(range(10), 7)
print(generate_unique_random_numbers())