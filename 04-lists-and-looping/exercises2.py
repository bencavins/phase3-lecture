# Task: rewrite each list comprehension as a for loop


# 1. simple copy
old_array = [1, 2, 3, 4, 5]
new_array = [item for item in old_array]
print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [1, 2, 3, 4, 5]


# 2. square each number
old_array = [1, 2, 3, 4, 5]
new_array = [item ** 2 for item in old_array]
print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [1, 4, 9, 16, 25]


# 3. filter out numbers greater than 3
old_array = [1, 2, 3, 4, 5]
new_array = [item for item in old_array if item <= 3]
print(old_array)  # [1, 2, 3, 4, 5]
print(new_array)  # [1, 2, 3]