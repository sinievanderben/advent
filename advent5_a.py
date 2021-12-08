
## Line segements 1 --> line segments 2
import numpy as np 

# read in the document
with open('/Users/sinievanderben/Documents/advent/test_day5.txt', 'r') as f:
    lines = f.readlines()

    lineArray = np.empty((10,10))

    max_num = 0 

    for line in lines:
        lineCoords = line.split()

        x1 = int(lineCoords[0].split(',')[0])
        y1 = int(lineCoords[0].split(',')[1])
        x2 = int(lineCoords[2].split(',')[0])
        y2 = int(lineCoords[2].split(',')[1])

        # Vertical Lines 
        if x1 == x2:
            
            difference = abs(y2 - y1)

            if y1 > y2:
                for i in range(y2, y1+1):
                    lineArray[x1][i] = lineArray[x1][i] + 1
            if y1 < y2:
                for i in range(y1, y2+1):
                    lineArray[x1][i] = lineArray[x1][i] + 1            
        
        # Horizontal lines 
        elif y1 == y2:
            difference_y = abs(x2 - x1)

            if x1 > x2:
                for j in range(x2, x1+1):
                    lineArray[j][y1] = lineArray[j][y1] + 1
            if x1 < x2:
                for j in range(x1, x2+1):
                    lineArray[j][y1] = lineArray[j][y1] + 1      

print(lineArray)

count = np.count_nonzero(lineArray > 1)
print("Total lines cross more than 1 time: ", count)

## consider only cases where x=x2 or y1-y2

## create empty numpy array of 10 by 10 

##for each pair that create a line

# check is x or y differs

# start at starting point and 