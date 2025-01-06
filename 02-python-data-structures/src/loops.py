l = [
    {
        'name': 'bob',
        'age': 50,
    },
    {
        'name': 'alice',
        'age': 40,
    },
    {
        'name': 'charlie',
        'age': 35,
    },
]


# loop over array without index
def simple_loop(array):
    for person in array:
        print(person)

####
#### MAP
####
def get_names(array):
    new_array = []  # create an empty array
    for person in array:  # loop over all items in array
        new_array.append(person['name'])  # add something to new array
    return new_array  # return new array

# print(get_names(l))

def get_names_upper(array):
    new_array = []  # create an empty array
    for person in array:  # loop over all items in array
        new_array.append(person['name'].upper())  # add something to new array
    return new_array  # return new array

# print(get_names_upper(l))


####
#### FILTER
####
def above_40(array):
    new_array = []
    for person in array:
        if person['age'] >= 40:  # check a condition
            new_array.append(person)
    return new_array

# print(above_40(l))


####
#### FILTER and MAP
####
def upper_name_above_40(array):
    new_array = []
    for person in array:
        if person['age'] >= 40:  # check a condition
            new_array.append(person['name'].upper() + '!')
    return new_array

# print(upper_name_above_40(l))


####
#### MIN/MAX
####
def get_youngest(array):
    youngest = array[0]  # initialize the youngest person
    for person in array:  # loop through all people
        if person['age'] < youngest['age']:  # compare the ages
            youngest = person  # replace if younger person is found
    return youngest  # return youngest

# print(get_youngest(l))


# a slick alternative
print(min(l, key=lambda x: x['age']))
print(max(l, key=lambda x: len(x['name'])))
