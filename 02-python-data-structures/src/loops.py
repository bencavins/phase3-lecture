data = [
    {
        'name': 'alice',
        'age': 34
    },
    {
        'name': 'bob',
        'age': 66
    },
    {
        'name': 'charlie',
        'age': 3
    }
]


# calculate average
total = 0
# count = 0
for person in data:
    total += person['age']
    # count += 1

print(total / len(data))


# map list[dict] -> list[str]
new_list = []
for person in data:
    new_list.append(person['name'])

# list comprehension form of the above loop
new_list = [person['name'] for person in data]


# filter
new_list = []
for person in data:
    if person['age'] >= 21:
        new_list.append(person)

# new_list = [person for person in data if person['age'] >= 21]
print(new_list)



