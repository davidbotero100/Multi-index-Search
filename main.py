# Multi-index-Search algorithm version 0.1

import numpy as np
from random import sample, shuffle, randint
from pytictoc import TicToc

# Declare Array of data
'''
array = []
values  =1

for i in range(0, 100):
    array.append(values + (i+5))

'''

#Better create classes and functions.

class multiIndex(): 

    # List of integers
    data = []

    #Dictionary of indecies
    indecies = dict( i=0, j=0, k=0, m=0,
                    l=0, n=0, p=0, o=0, )

    """
    i = size -1
    j =0

    k = size//4
    m = k

    l = size//2
    n = k

    p = size - k
    o = p
    """

       
    def getUserInput(self) -> int:

        self.numbers = input('Enter the number of elements: ')

        #print(self.numbers)

        # Convert str user input
        self.converted_numbers = int(self.numbers)

        return self.converted_numbers
               

    def fillList(self, numbers: int) -> None:

        local_list = []

        #converted_int = int(numbers)

        for i in range(numbers):
            local_list.append(i)
                
        #self.data = shuffle(local_list)

        self.data.extend(local_list)
        #print(*self.data)

        #print(*self.data)

    def shuffle(self, times: int = 100 ) -> None:
         
        for i in range(times):
            shuffle(self.data)

    # For testing index updates
    def testIndecies(self) -> None:
        
        for i in range(5):
            self.indecies['i'] += 2
            self.indecies['j'] += 1
        print(f"After iteration {i + 1}: {self.indecies}")

    def setIndecies(self, numbers: int) -> None:

        list_size = numbers

        self.indecies['i'] = 0

        self.indecies['j'] = list_size//4
        self.indecies['k'] = list_size//4+1

        self.indecies['m'] = list_size//2
        self.indecies['n'] = list_size//2+1

        self.indecies['l'] = list_size


    
if __name__ == '__main__':
        
    t = TicToc()
    t.tic()

    mi = multiIndex()

    numbers = mi.getUserInput()
    
    #converted_numbers = int(numbers)
    mi.fillList(numbers)

    # For testing only
    # mi.testIndecies()

    mi.setIndecies(numbers)

    t.toc()

    pass


           

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

