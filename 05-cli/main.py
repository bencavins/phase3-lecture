import random
import sqlite3
from sql import create_table, insert_score
from colorama import Fore, Style


conn = sqlite3.connect('scores.db')
cursor = conn.cursor()


def main():
    secret_number = random.randint(0, 100)
    guess_count = 0
    print(f'secret number is: {secret_number}')

    while True:
        guess = int(input('Enter a number between 0 and 100: '))
        guess_count += 1
        
        if guess == secret_number:
            print(Fore.GREEN + f'You win! It took {guess_count} guesses!' + Style.RESET_ALL)
            name = input('Enter your name: ')
            cursor.execute(insert_score, (name, guess_count))
            conn.commit()
            return
        elif guess < secret_number:
            print(Fore.RED + 'Too low' + Style.RESET_ALL)
        else:  # guess > secret_number
            print(Fore.RED + 'Too high' + Style.RESET_ALL)


if __name__ == '__main__':
    cursor.execute(create_table)
    main()
