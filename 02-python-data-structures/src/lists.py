my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
'c' in my_list

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'a')

# Merge two lists together
[1, 2, 3] + [4, 5, 6]

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]
my_list[0] = 'A'  # replace value at this index

# Slice
my_list[3:5]

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index('d')  # finds first instance only

# Count number of instances of an element
my_list.count(3)

# Remove element from list
my_list.pop()  # remove last item
my_list.pop(0) # remove item at index 0

# Sorting (with an without a key)

# sorted() vs .sort()
my_list.sort()
sorted(my_list)