import random
import sys

cyan = '\033[96m'
end = '\033[0m'

def main(target):
    # print(target)
    while True:
        answer = input('Pick a number between 1-100: ')
        if answer == 'q':
            print('quitting...')
            break

        answer = int(answer)
        if answer == target:
            print(f'{cyan}you guessed right!{end}')
            break
        elif answer < target:
            print('too low')
        elif answer > target:
            print('too high')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        rand_target = random.randint(1, 100)
        main(target=rand_target)
    else:
        user_target = int(sys.argv[1])
        main(target=user_target)
    print('done')
