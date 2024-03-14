# map
# transform every item in our collection
# loop through the original array
#   transform each item in the array
#   append each item in a new array
old_array = ['a', 'b', 'c', 'd', 'e', 'f']
new_array = []
for item in old_array:
    new_value = item.upper()
    new_array.append(new_value)

print(old_array)  # ['a', 'b', 'c', 'd', 'e', 'f']
print(new_array)  # ['A', 'B', 'C', 'D', 'E', 'F']


# filter
# loop through every item in the original array
#   test the item with a condition (if statement)
#   if it passes our condition, add it to a new array
old_array = [1, 2, 3, 4, 5, 6, 7, 8]
new_array = []
for item in old_array:
    if item % 2 == 0:  # check if the number is even
        new_array.append(item)

print(old_array)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(new_array)  # [2, 4, 6, 8]