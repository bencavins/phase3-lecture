my_dict = {
    'name': 'alice',
    'age': 34,
    'birthday': 'april',
}

# get value by key
my_dict['name']

# Add a key/value pair
my_dict['newkey'] = 'newvalue'

# Update a value
my_dict['name'] = 'bob'

# Use an invalid key
my_dict['badkey']  # KeyError

# Test if a key exists
'badkey' in my_dict

# use .get()
my_dict.get('somekey', 'default_value')

# Delete a key
my_dict.pop('key')
del my_dict['key']

# get the length of a dict
len(my_dict)

# TODO Merge two dicts

# copy a dict
my_dict.copy()

# loop over a dict
for key in my_dict:
    value = my_dict[key]
    print(key, value)