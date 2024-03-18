# List Comprehension
# has three parts: 2 required, 1 optional
# [(data to append) (for loop definition) (optional condition)]


# loop without a list comprehension
old_array = [1, 2, 3, 4, 5]
new_array = []
for item in old_array:  # for loop definition
    new_array.append(item)  # data append

print(old_array)
print(new_array)


# same loop with a list comprehension
old_array = [1, 2, 3, 4, 5]
new_array = [item for item in old_array]
print(old_array)
print(new_array)
