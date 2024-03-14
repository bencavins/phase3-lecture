# Task: rewrite each loop as a list comprehension

# 1. simple copy
old_array = [1, 2, 3, 4, 5]
new_array = []
for item in old_array:
    new_array.append(item)

print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [1, 2, 3, 4, 5]


# 2. double each number
old_array = [1, 2, 3, 4, 5]
new_array = []
for item in old_array:
    new_array.append(item * 2)

print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [2, 4, 6, 8, 10]


# 3. filter out odd numbers
old_array = [1, 2, 3, 4, 5]
new_array = []
for item in old_array:
    if item % 2 == 0:
        new_array.append(item)

print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [2, 4]