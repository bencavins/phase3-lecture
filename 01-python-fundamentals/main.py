# simple function with parameter
def hello(name):
    print('hello')  
    print(name)  # function code

hello('bob')
hello('alice')

# type conversion
x = '123'
print(type(x))

x = int(x)
print(type(x))


# while loop
x = 0
while x < 5:
    print(x)
    x += 1  # x = x + 1

print('outside the looop')

# for loop
l = [1, 2, 3, 4]
total = 0
for num in l:
    total += num
    # print(num, total)  # print debug

print(total) # 10


# if/else
x = 5
if x >= 1 and x <= 10:
    print('between 1 and 10')
else:
    print('not :(')

# you can also do this
if 1 <= x <= 10:
    print('between 1 and 10')
else:
    print('not :(')


# filter
def print_evens(some_list):
    for num in some_list:
        if num % 2 == 0:
            print(num)

print_evens([1, 2, 3, 4])
print_evens([1, 3, 5, 7, 0])


# for loop with range
# range(start, stop, step)
for i in range(0, 10, 3):
    print(i)
