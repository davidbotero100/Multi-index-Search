# Multi-index-Search algorithm version 0.1
import numpy as np

# Declare Array of data
'''
array = []
values  =1

for i in range(0, 100):
    array.append(values + (i+5))

'''

#Better create classes and functions.

# Fill 1D array with random ints between 0 and 100 for now
size = 100

# Format is: (range, (rows, columns))
rand_arr = np.random.randint(0, 100, (size))

# Declare indexes at each quarters of the array
i = size -1
j =0

k = size//4
m = k

l = size//2
n = k

p = size - k
o = p

# Get user input
searchVal  = input("Enter value to search: ")

for s in range(size // 4 + 1):
    if (rand_arr[int(i % size)] == searchVal or rand_arr[int(j % size)] == searchVal or
            rand_arr[int(k % size)] == searchVal or rand_arr[int(m % size)] == searchVal or
            rand_arr[int(n % size)] == searchVal or rand_arr[int(l % size)] == searchVal or
            rand_arr[int(o % size)] == searchVal or rand_arr[int(p % size)] == searchVal):
                print("Found in position", rand_arr.index(searchVal))
    i -= 1
    j += 1
    k -= 1
    m += 1
    n -= 1
    l += 1
    o -= 1
    p += 1


#print(rand_arr)

