# while loop
# don't know how many loop cycles are needed
# but know when to stop
x = 12345
count = 0
while x >= 1:
    x = x / 2  # x /= 2
    print(x)
    count += 1

print(f'this took {count} loop cycles')


# for loop
# looping over a data structure
# looping a specific number of times
for i in range(0, 10):
    print(i)


# looping over a list using indices
l = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(0, len(l)):
    print(i, l[i])

# without using indices
for item in l:
    print(item)


# looping over a dictionary
d = {
    'name': 'joe',
    'age': 56,
    'grades': [1, 2, 3]
}
for key in d:
    print(key, d[key])


# map
# transform every item in our collection
# loop through the original array
#   transform each item in the array
#   append each item in a new array
l = ['a', 'b', 'c', 'd', 'e', 'f']
result = []
for item in l:
    new_value = item.upper()
    result.append(new_value)
print(l)
print(result)


# filter
# loop through every item in the original array
#   test the item with a condition (if statement)
#   if it passes our condition, add it to a new array
l = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
for item in l:
    if item % 2 == 0:
        result.append(item)
print(l)
print(result)