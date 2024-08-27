# creating sets
my_set = set([1, 2, 3])
my_set = {1, 2 ,3}

# sets deduplicate data
my_set = set([1, 2, 2, 3, 4, 4])
print(my_set)  # {1, 2, 3, 4}

# find common elements between two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection(s2)  # {3}


# python docs on sets:
# https://docs.python.org/3.8/library/stdtypes.html#set