# Multi-Index-Search Algorithm Version 0.1

import numpy as np
from random import sample, shuffle, randint
from pytictoc import TicToc


class multiIndex(): 

    # Variable Declarations-------------------------------------

    # List of integers selected by user
    data = []

    #Dictionary of indicies
    indicies = dict( i=0, j=0, k=0, l=0,
                    m=0, n=0, o=0, p=0, )
    #-----------------------------------------------------------
     
    def getUserList(self) -> int:

        self.numbers = input('Enter the number of elements: ')

        #print(self.numbers)

        # Convert str user input to int
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
            

    # For testing index updates
    def testindicies(self) -> None:
        
        for i in range(5):
            self.indicies['i'] += 2
            self.indicies['j'] += 1
        print(f"After iteration {i + 1}: {self.indicies}")


    def setIndicies(self, numbers: int) -> None:

        list_size = numbers

        third_quarter = (list_size * 3) // 4

        self.indicies['i'] = 0

        self.indicies['j'] = list_size//4
        self.indicies['k'] = list_size//4+1

        self.indicies['l'] = list_size//2
        self.indicies['m'] = list_size//2+1

        self.indicies['n'] = third_quarter
        self.indicies['o'] = third_quarter+1

        self.indicies['p'] = list_size-1


    def getUserValue(self) -> int:
         
         i = 0
         
         while i < 1:
            
            userStr = input('Enter value to search: ')

            userVal = int(userStr)

            if (userVal >= len(self.data)):
                print('Value must be less than', len(self.data))

            elif (userVal < len(self.data)):
                i = 1


         return userVal



    
    def findValue(self, searchVal: int, numbers: int) -> None:
         
         list_size = len(self.data)
         quarter = list_size // 4
         half = list_size // 2
         third_quarter = (list_size * 3) // 4

         
         
         for x in range(numbers):
              
              if (searchVal == self.data[self.indicies['i']] or searchVal == self.data[self.indicies['j']] or
                  searchVal == self.data[self.indicies['k']] or searchVal == self.data[self.indicies['l']] or
                  searchVal == self.data[self.indicies['m']] or searchVal == self.data[self.indicies['n']] or
                  searchVal == self.data[self.indicies['o']] or searchVal == self.data[self.indicies['p']]):

                  print('Item found it in iteration ', x)
                  break
              
              else:
                  # Update indices within their quarters
            
                  self.indicies['i'] = min(self.indicies['i'] + 1, (list_size//8))

                  self.indicies['j'] = max(self.indicies['j'] - 1, (list_size//8))
                  self.indicies['k'] = min(self.indicies['k'] + 1, quarter)

                  self.indicies['l'] = max(self.indicies['l'] - 1, quarter)
                  self.indicies['m'] = min(self.indicies['m'] + 1, half)

                  self.indicies['n'] = max(self.indicies['n'] - 1, third_quarter)
                  self.indicies['o'] = min(self.indicies['o'] + 1, third_quarter)

                  self.indicies['p'] = max(self.indicies['p'] - 1, third_quarter)
    
if __name__ == '__main__':

    mi = multiIndex()

    numbers = mi.getUserList()
    
    #converted_numbers = int(numbers)
    mi.fillList(numbers)
    mi.shuffle()
    #print('Shuffled list is:', *mi.data)

    # For testing only
    # mi.testindicies()

    mi.setIndicies(numbers)
    searchValue = mi.getUserValue()
    #mi.testindicies()

    mi.findValue(searchValue, numbers)