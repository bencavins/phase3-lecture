# can build strings with single quotes
my_string = 'hello'
# or double quotes
another_string = "hello"
# or triple quotes
yet_another_string = '''hello'''

# Get length of string
len(my_string)

# Index into string
my_string[0]

# Slice string
my_string[0:4]

# Upper/Lowercase string
my_string.upper()
my_string.lower()

# Check if substring exists
if 'ell' in my_string:
    print('substring exists!')

# Loop over string
for char in my_string:
    print(char)