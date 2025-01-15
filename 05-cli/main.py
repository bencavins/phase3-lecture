def f():
    pass


if __name__ == '__main__':
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if not age.isdigit():
        print('Age needs to be a number!')
        exit()

    age = int(age)

    print(type(name))
    print(type(age))

    print(f'Hello, {name}! {age} years old')