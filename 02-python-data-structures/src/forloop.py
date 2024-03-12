my_seq = [1, 2, 3, 4, 5]

# looping style 1 (less common)
i = 0
while i < len(my_seq):  # loop until we run out of indices
    print(my_seq[i])  # print the char at this index
    i += 1  # increment the index

# looping style 2 (more common)
for i in range(len(my_seq)):  # loop over number range (from 0 to length of string - 1)
    print(f'i=={i} char=={my_seq[i]}')

# looping style 3 (also common, no indices)
for char in my_seq:
    print(char)
