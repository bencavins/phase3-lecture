my_dict = {
    'name': 'joe',
    'age': 55
}

# Key lookup
my_dict['name']

# Add a key/value pair
my_dict['phone'] = '555-555-5555'

# Update a value
my_dict['phone'] = '555-555-5555'

# Use an invalid key
my_dict['badkey']  # raises KeyError

# Test if a key exists
'name' in my_dict

# use .get()
my_dict.get('badkey')
my_dict.get('badkey', 'missing value')  # second arg is default value

# Delete a key
my_dict.pop('age')
del my_dict['age']

# get the length of a dict
len(my_dict)

# Merge two dicts
my_dict.update({'age': 6, 'phone': '555-555-5555'})

# copy a dict
my_dict.copy()

# TODO loop over a dict
