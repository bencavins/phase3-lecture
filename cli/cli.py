import sys

prompt = """
Pick one:
1) print hi
2) quit
"""

def run():
    while True:
        choice = input(prompt)
        if choice == '1':
            print('hi')
        else:
            break


if __name__ == '__main__':
    print(sys.argv)
    run()
