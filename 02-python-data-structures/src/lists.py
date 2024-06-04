my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
'a' in my_list

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'x')

# Merge two lists together
[1, 2] + [3, 4]

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]
my_list[-1]

# Slice
my_list[1:4]

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index('b')  # only finds first instance

# Count number of instances of an element
my_list.count('a')

# Remove element from list
my_list.pop()
my_list.pop(0)  # can also provide an index

# Sorting (with an without a key)
# sorts the list in place
my_list.sort()
my_list.sort(reverse=True)

# sorted() vs .sort()
# returns a sorted copy of the list
sorted(my_list)
sorted(my_list, reverse=True)