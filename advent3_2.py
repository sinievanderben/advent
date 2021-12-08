

# start with full list of binary numbers
# consider the first bit of the numbers

# Oxygen generator value 
# Determine most common value of the current bit position and keep only numbers with that bit in that position. 
# if both are equally common, keep values with 1

# scrubber
# Determine least common value in the current bit position and keep only numbers with that bit in position 

# Loop to determine most common value per position 
import numpy as np
import statistics

from statistics import mode 


with open('/Users/sinievanderben/Documents/advent/advent_day3.txt', 'r') as f:
    lines = f.readlines()
    position = ''

    for i in range(0, 12):
        count0 = 0
        count1 = 0

        # Loop over all lines 
        for line in lines:
            if i >= 1:
                if line[0:i] == position:
                    if int(line[i]) == 0:
                        count0 = count0 + 1
                    if int(line[i]) == 1:
                        count1 = count1 + 1

            if i == 0:
                if line[i] == '0':
                    count0 = count0 + 1
                if line[i] == '1':
                    count1 = count1 + 1

        print('count0 for ', i, ' is: ', count0)
        print('count1 for ', i, ' is: ', count1)

        if (count0 == count1):
            position = position + '1'

        if (count0 > count1):
            position = position + '0'

        if (count0 < count1):
            position = position + '1'

    generator_position = position 
    print('position generator', generator_position)  

f.close()

generator_int = int(generator_position, 2)
print(generator_int)

with open('/Users/sinievanderben/Documents/advent/advent_day3.txt', 'r') as f:
    lines = f.readlines()
    position = ''

    for i in range(0, 12):
        count0 = 0
        count1 = 0

        # Loop over all lines 
        for line in lines:
            if i >= 1:
                new_value = i -1
                if line[0:new_value] == position:
                    if int(line[i]) == 0:
                        count0 = count0 + 1
                    if int(line[i]) == 1:
                        count1 = count1 + 1

            if i == 0:
                if line[i] == '0':
                    count0 = count0 + 1
                if line[i] == '1':
                    count1 = count1 + 1

        print('count0 for ', i, ' is: ', count0)
        print('count1 for ', i, ' is: ', count1)

        if (count0 == count1):
            print('sim')
            print('before', position)
            position = position + '0'
            print('after',position)

        if (count0 > count1):
            position = position + '1'

        if (count0 < count1):
            position = position + '0'

    scrubber_position = position 
    print('position scrubber', scrubber_position)  

f.close()

generator_int = int(generator_position, 2)
scrubber_int = int(scrubber_position, 2)

total = generator_int * scrubber_int
print(total)