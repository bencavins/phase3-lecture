# 1. write a function that takes an array of numbers and squares each number
def get_sqares(numbers):
    # no comp
    square = []
    for num in numbers:
        square.append(num ** 2)
    return square

    # with comp
    return [num ** 2 for num in numbers]

# example
print(get_sqares([1, 2, 3, 4, 5]))
#=> [1, 4, 9, 16, 25]



# 2. write a function that filters out all the odd numbers
def get_evens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

    # with comp
    return [number for number in numbers if number % 2 == 0]

# example
print(get_evens([1, 2, 3, 4, 5]))
# #=> [2, 4]



# 3. write a function that takes an array of dicts and returns an
# array of the 'name' values
def get_names(people):
    array = []
    for item in people:
        array.append(item['name'])
    return array

    # with comp
    return [item['name'] for item in people]

test_data = [
    {
        'name': 'kermit',
        'age': 44,
    },
    {
        'name': 'mrs. piggy',
        'age': 36,
    },
    {
        'name': 'gonzo',
        'age': 22
    }
]

# example
print(get_names(test_data))
# #=> ['kermit', 'mrs. piggy', 'gonzo']



# 4. write a function that filters out all fruit that isn't red
def get_reds(fruits):
    result = []
    for fruit in fruits:
        if fruit['color'] == 'red':
            result.append(fruit)
    return result

    # with comp
    return [fruit for fruit in fruits if fruit['color'] == 'red']

test_data = [
    {
        'name': 'strawberry',
        'color': 'red',
    },
    {
        'name': 'banana',
        'color': 'yellow',
    },
    {
        'name': 'blueberry',
        'color': 'blue',
    },
    {
        'name': 'raspberry',
        'color': 'red',
    },
]

# example
print(get_reds(test_data))
# #=> [{'name': 'strawberry', 'color': 'red'}, {'name': 'raspberry', 'color': 'red'}]



# 5. write a function that returns only the *titles* of *nintendo* games (map and filter)
test_data = [
    {
        'title': 'legend of zelda',
        'platform': 'nintendo',
    },
    {
        'title': 'price of persia',
        'platform': 'playstation',
    },
    {
        'title': 'super mario bros',
        'platform': 'nintendo',
    },
    {
        'title': 'fortnite',
        'platform': 'all',
    },
]
def get_nintendo_titles(games):
    array = []
    for game in games:
        if game['platform'] == 'nintendo' or game['platform'] == 'all':
            array.append(game['title'])
    return array

    # with comp
    return [game['title'] for game in games if game['platform'] == 'nintendo' or game['platform'] == 'all']

# example
print(get_nintendo_titles(test_data))
# #=> ['legend of zelda', 'super mario bros', 'fortnite']  # <= tricky! fortnite counts!



# 6. write a function that returns the most expensive gemstone
test_data = [
    {
        'name': 'saphire',
        'price': 575.00,
    },
    {
        'name': 'ruby',
        'price': 999.99,
    },
    {
        'name': 'opal',
        'price': 225.00,
    },
    {
        'name': 'diamond',
        'price': 5999.99,
    },
]
def get_priciest_gemstone(gemstones):
    priciest = gemstones[0]
    for gem in gemstones:
        if gem['price'] > priciest['price']:
            priciest = gem
    return priciest

    # can't use list comp but can use fancy lambda function solution
    return max(gemstones, key=lambda gem: gem['price'])

# example
print(get_priciest_gemstone(test_data))
# #=> {'name': 'diamond', 'price': 5999.99}


# BONUS CHALLENGE!
# If you are comfortable with writing the above loops,
# try using a list comprehension for each! (Can't with #6)