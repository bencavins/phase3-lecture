my_dict = {
    'name': 'joe',
    'age': 30
}

# Add a key/value pair
my_dict['key'] = 123456789

# Update a value
my_dict['key'] = 123456789

# Use an invalid key
my_dict['badkey']  # raises KeyError

# Test if a key exists
'badkey' in my_dict

# use .get()
my_dict.get('key', 'defaultvalue')
my_dict.setdefault('key', 'defaultvalue')  # actually sets the key/value pair

# Delete a key
my_dict.pop('badkey')

# get the length of a dict
len(my_dict)

# Merge two dicts
my_dict.update({'height': 123})

# copy a dict
my_dict.copy()

# loop over a dict
for key in my_dict:
    print(key, my_dict[key])  # key, value