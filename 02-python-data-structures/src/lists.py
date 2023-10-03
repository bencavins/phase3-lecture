my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
'a' in my_list

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'zzz')

# Merge two lists together
my_list + ['x', 'y', 'z']

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]

# Slice [start:stop:step]
my_list[0:3]

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index('c')

# Count number of instances of an element
my_list.count('c')

# Remove element from list
my_list.pop()

# TODO Sorting (with an without a key)

# sorted() vs .sort()
my_list.sort() # destructive
sorted(my_list) # non-destructive

my_list.sort(reverse=True) # destructive
sorted(my_list, reverse=True) # non-destructive