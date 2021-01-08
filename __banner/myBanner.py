import colorama
import random
import sys

def bannerTop():
    banner = '''
******************************************...****
*              EDU-MAIL GENERATOR               *        
*                                               *
*              By- @aniruddhsinghal5            *
******************************************...****
      Github Repostory - https://github.com/aniruddhsinghal5/edumailgen\n\n
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)
