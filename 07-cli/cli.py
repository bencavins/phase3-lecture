import random
import os


def get_target():
    target = random.randint(1, 100)
    # print(f'target number is: {target}')
    return target

def check_input(value, target):
    if value == target:
        print('you win!')

        answer = input('do you want to play again? (y/n) ')
        if answer == 'y':
            target = get_target()
            return True  # still playing
        else:
            return False  # not playing anymore
    elif value < target:
        print('too low')
        return True  # still playing
    else:
        print('too high')
        return True  # still playing



def run():
    is_playing = True
    target = get_target()


    s = """
       ___           ___           ___           ___           ___     
      /\__\         /\  \         /\__\         /\__\         /\__\    
     /:/ _/_        \:\  \       /:/ _/_       /:/ _/_       /:/ _/_   
    /:/ /\  \        \:\  \     /:/ /\__\     /:/ /\  \     /:/ /\  \  
    /:/ /::\  \   ___  \:\  \   /:/ /:/ _/_   /:/ /::\  \   /:/ /::\  \ 
    /:/__\/\:\__\ /\  \  \:\__\ /:/_/:/ /\__\ /:/_/:/\:\__\ /:/_/:/\:\__\
    \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  /
    \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \::/ /:/  /   \::/ /:/  / 
    \:\/:/  /     \:\/:/  /     \:\/:/  /     \/_/:/  /     \/_/:/  /  
        \::/  /       \::/  /       \::/  /        /:/  /        /:/  /   
        \/__/         \/__/         \/__/         \/__/         \/__/   
    """
    # print(s)

    while is_playing:
        # os.system('clear')
        value = input("Enter a number (type 'q' to quit): ")

        if value == 'q':
            print('user quit')
            exit()

        value = int(value)
        is_playing = check_input(value, target)
        
    print('done')


if __name__ == '__main__':
    run()
