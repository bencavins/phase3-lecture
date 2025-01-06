
def add(x, y):
    return x + y

def hello_world():
    print('hello world!')


s1 = 'hello'  # can use single quotes
s2 = "hello"  # can use double quotes
s3 = '''h
e
l
l
o'''  # triple quotes can be on multiple lines
s4 = 'can\'t do that'  # escape chars with \

a = 1  # int
b = 3.14 # float
c = 'hello' # str
d = True  # bool
e = [1, True, 'hello']  # list
f = {'name': 'bob', 'age': 50} # dict
g = None # NoneType

# print(type(g))  # type() func returns the data type 
# print(isinstance(a, int))  # isinstance() returns True/False based on if the data type matches

# print(add(5, 6))
# print(add('5', '6'))
# print(add([5], [6]))
# print(add(True, False))


# print(add(int('5'), 6))  # type conversion


x = 100

# if x < 10:
#     print('small')
#     print(':)')
# elif x >= 10 and x < 20:
#     print('medium')
#     print(':|')
# elif x == 100:
#     print('hundred')
# else:
#     print('big')
#     print(':(')

# print('code bock ends')

# y = 50
# y < 10 ? 'less' : 'more'
# print('less' if y < 10 else 'more')


# x = 0
# while x < 5:
#     print(x)
#     x += 1


l = ['a', 'b', 'c', 'd']

# for loop with range and indexes
# for i in range(0, len(l)): # range(0, 4) => [0, 1, 2, 3]
#     print(i, l[i])

# easy for loop
# for value in l:
#     print(value + '!')


def sum(values):
    total = 0
    for x in values:
        total += x  # total = total + x
    return total

# print(sum([1, 2, 3]))
# print(sum([99, 100, 101]))


people = [
    {'name': 'bob', 'age': 50},
    {'name': 'alice', 'age': 40},
    {'name': 'charlie', 'age': 30},
]

def print_name(people):
    for person in people:
        print(person['name'])

