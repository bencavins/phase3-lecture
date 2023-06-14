my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Test if an element exists in `my_list`
'a' in my_list

# Add element to the end
my_list.append('h')

# Insert element at an index
my_list.insert(0, 'zzz')

# Merge two lists together
[1, 2, 3] + [4, 5, 6]

# Duplicate a list
my_list.copy()

# Index lookup
my_list[0]

# Slice
my_list[0:2]

# Get length
len(my_list)

# Get min/max
min(my_list)
max(my_list)

# Find index of an element
my_list.index('a')

# Count number of instances of an element
my_list.count('a')

# Remove element from list
my_list.remove('a')

# Sorting (with an without a key)
my_list.sort()

# sorted() vs .sort()
sorted(my_list)

# list comprehension 
result = []
for num in range(0, 10):
    if True:
        result.append(num * 2)

result2 = [x for x in range(0, 10)]
print(result2)