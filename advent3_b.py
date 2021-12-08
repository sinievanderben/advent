import numpy as np


with open('/Users/sinievanderben/Documents/advent/advent_day3.txt', 'r') as f:
    lines = f.readlines()

    for i in range(11):
        print(i)
        

        countZeros = 0
        countOnes = 1

        new_lines = []

        for x in lines:
            new_lines.append(x.strip())

    
        # loop over all lines to determine 
        for line in new_lines:

            # check if element is 0 or 1 for i == 1
            if i == 0:
                ## Add 1 for all zeros
                if line[i] == "0":
                    countZeros += 1
                ## Add 0 for all ones    
                if line[i] == "1":
                    countOnes += 1
            
            # check if element is 0 or 1 for i > 1
            # take elements before into account 
            if i > 0:

                if line[:i] == position:

                    ## Add 1 for all zeros
                    if line[i] == "0":
                        countZeros += 1
                    ## Add 0 for all ones    
                    if line[i] == "1":
                        countOnes += 1

        
        # After looping over all lines, compare counts
        if i == 0:
            if countZeros == countOnes:
                position = '0'
            if countZeros < countOnes:
                position = '0'
            if countZeros > countOnes:
                position = '1'

        else:
            if countZeros == countOnes:
                position = position + '0'
            if countZeros < countOnes:
                position = position + '0'
            if countZeros > countOnes:
                position = position + '1'
        
        # Check is previous elements match alreay acquired elements 

    for line in new_lines:
        if line[:11] == position:
            print('this line:', line)
            bestline = line

                    
print('position length ', len(position))
generator_int = int(bestline, 2)

print(generator_int)
                    
#2804
#1601
print(2804*1601)
