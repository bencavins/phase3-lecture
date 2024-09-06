import random
import sqlite3


conn = sqlite3.connect('guess.db')


def create_scores_table():
    sql = """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            username TEXT,
            score INTEGER
        )
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def add_score(username, score):
    """Adds username and score to the db"""
    sql = """
        INSERT INTO scores (username, score)
        VALUES (?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, [username, score])
    conn.commit()


def play():
    target = random.randint(1, 100)
    guess_count = 0
    # print(f'the secret number is {target}')

    # gameplay loop
    while True:
        guess = int(input('Guess a number: '))
        guess_count += 1
        
        if guess == target:
            print('you win!')
            print(f'took {guess_count} guesses')

            name = input('Enter your name: ')
            add_score(name, guess_count)

            return
        elif guess < target:
            print('too low')
        else:  # guess > target
            print('too high')


def run():
    create_scores_table()

    while True:
        prompt = """
Select an option:
1. Play game
2. Print scores
3. Quit
>> """
        option = input(prompt)
        if option == '1':
            play()
        elif option == '2':
            print('printing scores')
        else:
            print('quitting')
            exit()


print(__name__)
# this will only run if i do python cli.py, will not run if i import from this file
if __name__ == '__main__':
    run()
