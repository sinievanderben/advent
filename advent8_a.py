
# Each entry constists of 10 unique signal patterns, delimiter and the 4 digit output value. 

# 7 has 3 signals
# 4 has 4 signals
# 8 has 7 signals
# 1 has 2 signals

import numpy as np

with open('/Users/sinievanderben/Documents/advent/advent_day8.txt', 'r') as f:
    lines = f.readlines()

    count = 0

    for line in lines:

        splitted_line = line.split()

        for digit in splitted_line[11:]:
            if len(digit) == 2:
                count = count + 1
                print(1)
            if len(digit) == 3:
                count = count + 1
                print(7)
            if len(digit) == 4:
                count = count +1
                print(4)
            if len(digit) ==  7:
                count = count + 1
                print(8)
            else:
                print("no number")
                print(digit)
    

    print(count)
f.close()

        