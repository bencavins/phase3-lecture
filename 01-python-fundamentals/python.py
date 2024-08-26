# Variables
my_var = 1  # we use snake case in Python
MY_CONSTANT = "don't change me!"  # All variables are changeable in Python, programmers use all caps to signal when something should be a constant

# Functions
def my_func(param1, param2):
    pass # do something


# Simple data types
my_int = 0
my_float = 3.14
my_bool = True
my_string = "hello"  # or 'hello' or '''hello'''
my_list = [1, 2, 3, 4]
my_dictionary = {'name': 'joe', 'age': 21}
my_none = None


# Type checking
type(my_int)

# Type conversion
int('1')
float('3.14')
str(1234)
bool(99)


# Printing
print('print me!')

# Arrays/Lists
array_abc = ['a', 'b', 'c']
array_abc[0]  # => 'a'
array_abc[0] = 'z'  # ['z', 'b', 'c']
len(array_abc)  # => 3
array_abc.append('d')  # ['z', 'b', 'c', 'd']

# JSON Objects/Dictionaries
my_dict = {
    "name": "joe",
    "age": 44
}
my_dict['newkey'] = 'new value'
my_dict['badkey']  # raises KeyError

# Conditionals
if True:
    pass  # do something
elif False:
    pass  # do something else
else:
    pass  # catch-all


# Comparison Operators
10 < 15   # less than => True
10 > 15   # greater than => False
4 <= 4    # less than/equal => True
4 >= 5    # greather than/equal => False
12 == 12  # equal => True
12 != 12  # no equal => False

# Logical Operators
True and True  # AND => True
True or False  # OR => True
not True       # NOT => False

# while loop
while False:
    pass  # loop code


# for loop
for i in range(0, 10):
    pass  # loop code


# for item in collection
seq = ['a', 'b', 'c']
for char in seq:
    pass  # loop code


