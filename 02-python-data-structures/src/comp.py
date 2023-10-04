my_list = [1, 2, 3, 4, 5, 6]
result = []
for number in my_list:
    if number % 2 == 0:  # the number is even
        result.append(number * 2)
print(result)

# [(transformation) (looping def) (condition/filter *optional*)]
result = [number * 2 for number in my_list if number % 2 == 0]
print(result)
