my_str = 'hello world!'

# https://docs.python.org/3/library/stdtypes.html#string-methods

# Index lookup
my_str[0]  # h
my_str[0:5] # hello

# Concatenation
s1 = 'hello'
s2 = s1 + '!'  # hello!

w1 = 'hello'
w2 = 'world'
w1 + ' ' + w2 # hello world

# Format strings
w1 = 'hello'
w2 = 'world'
f1 = f'{w1} {w2}!'  # hello world!

# Some case methods
my_str.upper() # HELLO WORLD!
my_str.lower() # hello world!
my_str.capitalize() # Hello world!
my_str.title() # Hello World!

# Split
s1 = 'hello from flatiron school'
s1.split() # ['hello', 'from', 'flatiron', 'school']
s2 = 'name,age,sign'
s2.split(',') # ['name', 'age', 'sign']

# Join
l1 = ['hello', 'world', 'again']
' '.join(l1) # 'hello world again'
