my_list = ['a', 'b', 'c', 'd']

# index lookup
print(my_list[0])
print(my_list[1])

# python supports negative indices
print(my_list[-1])
print(my_list[-2])

# add data
my_list.append('e')
my_list.insert(0, 'z')
print(my_list)

# remove data
my_list.pop()  # remove last item
my_list.pop(0) # remove by index
print(my_list)

# slicing
my_slice = my_list[-1:1:-1]
print(my_slice)

# get the length
print(len(my_list))

# looping
for value in my_list:
    print(value)