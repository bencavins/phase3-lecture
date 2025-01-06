my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Index lookup
my_list[0] # 'a'
my_list[-1] # 'g'

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'z')  # less efficient than append!

# Get length
len(my_list) # 7

# Test if an element exists in `my_list`
'a' in my_list  # True
'z' not in my_list  # False

# Find index of an element
my_list.index('a')  # 0
# only returns the first instance!

# Merge two lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # [1, 2, 3, 4, 5, 6]

# Slice
my_list[1:3]  # ['b', 'c']

# Remove element from list
my_list.pop(0)  # deletes 'a'
my_list.remove('d')  # deletes 'd'

# Duplicate a list
my_list.copy()

# Get min/max
a = [1, 2, 3, 4]
min(a) # 1
max(a) # 4

# Count number of instances of an element
a = ['a', 'a', 'b', 'c', 'c', 'c']
a.count('c')  # 3

# Sorting (with an without a key)
my_list.sort()

# TODO sorted() vs .sort()