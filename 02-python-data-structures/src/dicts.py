my_dict = {
    'id': 1,
    'name': 'joe',
    'age': 44.5,
    'list': [1, 2, 3]
}

p2 = {
    'id': 2,
    'name': 'anne',
    'age': 34,
    'list': [1, 2, 3]
}

# get value at key
my_dict['id']

# Add a key/value pair
my_dict['newkey'] = 'newvalue'

# Update a value
my_dict['id'] = 99

# Use an invalid key
my_dict['missingkey']

# Test if a key exists
'id' in my_dict

# use .get()
my_dict.get('missing')
my_dict.get('missing', 'default value')

# get values
my_dict.values()

# Delete a key
my_dict.pop('newkey')

# get the length of a dict
len(my_dict)

# Merge two dicts
my_dict.update({'x': 'y'})

# copy a dict
my_dict.copy()

# loop over a dict
for key in my_dict:
    print(key, my_dict[key])  # print(key, value)

for key, value in my_dict.items():
    print(key, value)  # print(key, value)