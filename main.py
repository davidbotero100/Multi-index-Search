# Multi-Index-Search Algorithm Version 0.5

import numpy as np
from random import shuffle

class multiIndex(): 
    
    # Variable Declarations-------------------------------------

    # List of integers selected by user
    data = []
                    
    #-----------------------------------------------------------
    
     
    def getUserList(self) -> int:

        self.numbers = input('Enter the number of elements, greater than 8: ')

        while not self.numbers.isdigit() or int(self.numbers) < 8:
            print('Invalid input. Please enter a number greater than 8.')
            self.numbers = input('Enter the number of elements: ')

        self.converted_numbers = int(self.numbers)

        return self.converted_numbers
               

    def fillList(self, numbers: int) -> None:

        local_list = []

        for i in range(numbers):
            local_list.append(i)

        self.data.extend(local_list)


    def shuffle(self, times: int = 100 ) -> None:

        for i in range(times):
            shuffle(self.data)



    def setIndexes(self, numbers: int) -> None:

        if numbers < 8:
            print('List must have at least 8 elements.')
            exit()

        # Number of dynamic segments (pairs of indexes)
        num_segments = max(4, int(np.log2(numbers)))
        segment_size = numbers // num_segments

        # Dynamic start and end indexes for each segment
        self.indexes = {}
        for i in range(num_segments):
            start_key = f'start_{i}'
            end_key = f'end_{i}'
            self.indexes[start_key] = i * segment_size
            self.indexes[end_key] = min((i + 1) * segment_size - 1, numbers - 1)



    def getUserValue(self) -> int:
         
         i = 0
         
         while i < 1:
            
            userStr = input('Enter value to search: ')
            
            while not userStr.isdigit():
                print('Invalid input. Please enter a number.')
                userStr = input('Enter value to search: ')

            userVal = int(userStr)

            if (userVal >= len(self.data)):
                print('Value must be less than', len(self.data))

            elif (userVal < len(self.data)):
                i = 1


         return userVal


    def findValue(self, searchVal: int, numbers: int) -> None:

        for iteration in range(numbers):

            # Value found
            if any(searchVal == self.data[idx] for idx in self.indexes.values()):
                print(f'Item found in iteration {iteration}')
                break

            # Close in the indexes on their respective segments
            num_segments = len(self.indexes) // 2
            for i in range(num_segments):
                start_key = f'start_{i}'
                end_key = f'end_{i}'

                self.indexes[start_key] = min(self.indexes[start_key] + 1, self.indexes[end_key])
                self.indexes[end_key] = max(self.indexes[end_key] - 1, self.indexes[start_key])

    
if __name__ == '__main__':

    mi = multiIndex()

    numbers = mi.getUserList()
    
    mi.fillList(numbers)

    mi.shuffle()

    #print('Shuffled list is:', *mi.data)

    mi.setIndexes(numbers)

    searchValue = mi.getUserValue()

    mi.findValue(searchValue, numbers)