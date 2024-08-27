my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
'a' in my_list
'b' not in my_list

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'z')

# update a value by index
my_list[1] = 'some value'

# Merge two lists together
[1, 2, 3] + [4, 5, 6]

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]

# TODO Slice

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index('a')

# TODO Count number of instances of an element

# Remove element from list
my_list.remove('a')

# Sorting (with an without a key)
my_list.sort()

# TODO sorted() vs .sort()


# looping through list with while loop
my_list = ['a', 'b', 'c', 'd']
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


# range(0, 5)  # 0, 1, 2, 3, 4
# looping with indicies and range function
for i in range(0, len(my_list)):
    print(my_list[i])


# looping with for-each loop
for value in my_list:
    print(value)

# loop through list backward
for i in range(len(my_list)-1, -1, -1):
    print(my_list[i])

# also loop through list backward
# using crazy syntax
for item in my_list[::-1]:
    print(item)
