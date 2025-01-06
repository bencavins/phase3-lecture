# Sets
# all that is unique (no duplicates)
# no order to data

my_set = set()

# Add data to a set
my_set.add(3)

# Check if something exists in set
1 in my_set

# Dedupliate a list
no_dupe_set = set([1, 2, 3, 2, 1, 2, 3, 3, 2, 1])
no_dupe_list = list(set([1, 2, 3, 2, 1, 2, 3, 3, 2, 1]))