import sys

# argument vector for reading args/flags from the command line
# click library: https://click.palletsprojects.com/en/8.1.x/
print(sys.argv)

# Curses lib for painting:
# https://docs.python.org/3/howto/curses.html

# while True:
#     print('type "q" to exit')
#     number1 = input("Enter a number: ")
#     number2 = input("Enter another number: ")
#     if number1 == 'q' or number2 == 'q':
#         exit()
#     print('The sum is ' + str(int(number1) + int(number2)))

# how coloring works
# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux

import os
import time
while True:
    os.system('clear')
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    print(f"I {RED}love{NC} Stack Overflow\n")
    time.sleep(1)
    os.system('clear')
    print(f"I love Stack Overflow\n")
    time.sleep(1)
    


# nice lib for multiple choice:
# from pick import pick

# title = 'Please choose your favorite programming language: '
# options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
# option, index = pick(options, title)
# print(option)
# print(index)


print("""
  ___ ___ .___ 
 /   |   \|   |
/    ~    \   |
\    Y    /   |
 \___|_  /|___|
       \/      """)