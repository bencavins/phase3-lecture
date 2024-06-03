x = 7  # integer (int)
y = 3.14 # floating point number (float)
my_bool = False # boolean (bool)
my_string = "can't do this"  # string (str)
my_array = [1, 2, 3, 'hello', True]  # array (list)
my_dict = {  # dictionary (dict)
    'name': 'joe',
    'age': 55
}
my_none = None  # NoneType


def add(x, y):
    result = x + y
    return result

def hello_word():
    print('hello world!')

my_result = add(4, 5)
hello_word()


x = -1

if x > 10: 
    add(4, 5)
    print('great')
elif x < 0:
    print('neg')
else:
    print('mid')


def f():
    if y < 20:
        print('y < 20')

y = 30
if y > 10:
    print('y > 10')
    f()  # splitting code into functions helps reduce indents
else:
    print(':(')

# while loops are good when we don't know how many time we want to loop
# but he know when we want to stop
x = 123456
while x > 1:
    print(x)
    x = x / 12
    x += 1  # x = x + 1


# for loops are good for looping over a collection
my_numbers = [1, 2, 3, 4, 5]
for num in my_numbers:
    num = num * 2
    print(num)

print(len(my_numbers))

for i in range(0, len(my_numbers)):
    print(i, my_numbers[i])

print(my_numbers)