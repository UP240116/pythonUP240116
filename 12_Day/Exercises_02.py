#LEVEL 2
#1.Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors=1):
    """
    Generate a list of hexadecimal color codes.
    
    :param num_colors: Number of hex colors to generate (default is 1)
    :return: List of hex color codes
    """
    hex_digits = '0123456789abcdef'
        
    colors = []
    for _ in range(num_colors):
        
        color = '#' + ''.join(random.choice(hex_digits) for _ in range(6))
        colors.append(color)
        return colors
print(list_of_hexa_colors(3))

#2.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(num_colors=1):
    """
    Generate a list of RGB color codes.
    
    :param num_colors: Number of RGB colors to generate (default is 1)
    :return: List of RGB color codes
    """
    colors = []
    for _ in range(num_colors):

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        color = f'rgb({r},{g},{b})'
        colors.append(color)
        return colors
print(list_of_rgb_colors())  
print(list_of_rgb_colors(7))  
print(list_of_rgb_colors(6))  

#3.Write a function generate_colors which can generate any number of hexa or rgb colors.
import random

def generate_colors(color_type, num_colors=1):
    """
    Generate a list of colors (either hexadecimal or RGB).
    
    :param color_type: Type of colors to generate ('hexa' or 'rgb')
    :param num_colors: Number of colors to generate (default is 1)
    :return: List of color codes
    """
    # Validate input
    if color_type not in ['hexa', 'rgb']:
        raise ValueError("Color type must be 'hexa' or 'rgb'")
    
    # Hexadecimal digits
    hex_digits = '0123456789abcdef'
    
    # Generate colors
    colors = []
    for _ in range(num_colors):
        if color_type == 'hexa':
            # Generate hexadecimal color
            color = '#' + ''.join(random.choice(hex_digits) for _ in range(6))
        else: 
           
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f'rgb({r}, {g}, {b})'
        
        colors.append(color)
    
    return colors
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))