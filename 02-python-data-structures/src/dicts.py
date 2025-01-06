my_dict = {
    'name': 'bob',
    'age': 50,
    'sign': 'taurus',
    'job': 'taxi driver'
}

# Key lookup
my_dict['name']  # bob
my_dict['age']  # 50

# Test if a key exists
'name' in my_dict  # True

if 'name' in my_dict:
    print(my_dict['name'])

# Add a key/value pair
my_dict['id'] = 1234

# Update a value
my_dict['name'] = 'robert'

# Use an invalid key
my_dict['badkey']  # KeyError

# Delete a key
my_dict.pop('name')
del my_dict['name']

# use .get()
my_dict.get('name')
my_dict.get('name', 'default value')

# get the length of a dict
len(my_dict)

# copy a dict
my_copy = my_dict.copy()

# loop over a dict
for key in my_dict:  # can only loop over keys
    value = my_dict[key]  # use key to get value
    print(key, value)

# TODO Merge two dicts