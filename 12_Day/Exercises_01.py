#LEVEL 1
#1.Writ a function which generates a six digit/character random_user_id.
import random
import string

def random_user_id():

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(random_user_id())

#2.Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def user_id_gen_by_user():
    
    num_characters, num_ids = map(int, input("Enter number of characters and number of IDs (space-separated): ").split())
   
    user_ids = []
    for _ in range(num_ids):
       
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_characters))
        user_ids.append(user_id)
   
    return '\n'.join(user_ids)
print(user_id_gen_by_user())

#3.Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f'rgb({r},{g},{b})'
print(rgb_color_gen())


