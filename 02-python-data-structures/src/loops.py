my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# simple for loop (no indices)
# for item in my_list:
#     print(item)

# # for loop with indices
# for i in range(0, len(my_list)):
#     print(i, my_list[i])

# loop over dict
# my_dict = {
#     'name': 'joe',
#     'age': 55
# }
# for key in my_dict:
#     print(key, my_dict[key])

# # using .items()
# for key, value in my_dict.items():
#     print(key, value)


# map 
my_list = [1, 2, 3, 4, 5]

def double(numbers):
    """Double every number in numbers"""
    new_list = []  # create empty list
    for num in numbers:  # loop over every number
        new_num = num * 2  # transforming the number
        new_list.append(new_num)  # add to new_list
    return new_list

print(my_list)
print(double(my_list))


# filter
my_list = [1, 2, 3, 4, 5, -1, -2, 6, 7, -8]

def get_posis(numbers):
    """Returns a new list with negative numbers filtered out"""
    new_list = []  # create empty list
    for num in numbers:  # loop over existing list
        if num > 0:  # check condition
            new_list.append(num)  # add num to new list
    return new_list

print(my_list)
print(get_posis(my_list))


# min/max problem
my_list = [
    {
        'name': 'bob',
        'age': 12
    },
    {
        'name': 'joe',
        'age': 55,
    },
    {
        'name': 'anne',
        'age': 44
    }
]

current_max = my_list[0]
for current_item in my_list:
    if current_item['age'] > current_max['age']:
        current_max = current_item

print(current_max)