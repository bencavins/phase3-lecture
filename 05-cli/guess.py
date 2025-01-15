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

def get_scores():
    """Returns the scores from the scores table"""
    sql = """
        SELECT username, score
        FROM scores
        ORDER BY score
    """
    cursor = conn.cursor()
    return cursor.execute(sql).fetchmany(10)


def play():
    target = random.randint(1, 100)
    guess_count = 0
    # print(f'the secret number is {target}')

    # gameplay loop
    while True:
        # prompt the user to guess a number
        guess = int(input('Guess a number: '))  # pauses until user enters a value
        # increment the guess count
        guess_count += 1
        
        if guess == target:
            print('you win!')
            print(f'took {guess_count} guesses')

            name = input('Enter your name: ')
            # add the score to a db
            add_score(name, guess_count)

            return  # exit the play function
        elif guess < target:
            print('too low')
        else:  # guess > target
            print('too high')


def run():
    # create the scores table
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
            scores = get_scores()
            print('-'*20)
            for score in scores:
                print(score)
            print('-'*20)
        else:
            print('quitting')
            exit()


# this will only run if i do python cli.py, will not run if i import from this file
if __name__ == '__main__':
    run()
