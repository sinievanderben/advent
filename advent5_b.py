
## Line segements 1 --> line segments 2
import numpy as np 

# read in the document
with open('/Users/sinievanderben/Documents/advent/advent_day5.txt', 'r') as f:
    lines = f.readlines()

    lineArray = np.zeros((1000,1000))

    count = 0 

    print('horizontal and vertical')
    for line in lines:
        lineCoords = line.split()

        x1 = int(lineCoords[0].split(',')[0])
        y1 = int(lineCoords[0].split(',')[1])
        x2 = int(lineCoords[2].split(',')[0])
        y2 = int(lineCoords[2].split(',')[1])

        difference_y = abs(y2 - y1)
        processedLine = True

        while processedLine:

        # Vertical Lines 
            if x1 == x2:
                if y1 > y2:
                    print(line)
                    for i in range(y2, y1+1):
                        lineArray[x1][i] = lineArray[x1][i] + 1

                    count = count + 1
                    break

                if y1 < y2:
                    print(line)
                    for i in range(y1, y2+1):
                        lineArray[x1][i] = lineArray[x1][i] + 1  
                    count = count + 1
                    break    

            # Horizontal lines 
            elif y1 == y2:
                if x1 > x2:
                    print(line)
                    for j in range(x2, x1+1):
                        lineArray[j][y1] = lineArray[j][y1] + 1
                    count = count + 1
                    break

                if x1 < x2:
                    print(line)
                    for j in range(x1, x2+1):
                        lineArray[j][y1] = lineArray[j][y1] + 1   
                    count = count + 1
                    break

            if x1 > x2:
                if y1 > y2:
                    print(line)
                    for i in range(y2, y1+1):
                        
                        diff = i-y2
                        print(x1-diff)
                        print(y1-i)
                        lineArray[x1-diff][y1-diff] = lineArray[x1-diff][y1-diff] + 1
                    count = count + 1
                    break

                if y1 < y2:
                    print(line)
                    for i in range(y1, y2+1):
                        diff = i - y1
                        print(x1-diff)
                        print(i)
                        lineArray[x1-diff][i] = lineArray[x1-diff][i] + 1          
                    count = count + 1
                    break

            if x1 < x2:
                if y1 > y2:
                    print('this situation ')
                    print(line)
                    for i in range(y2, y1+1):
                        diff = i-y2
                        print(x1+diff)
                        print(y1-diff)
                        lineArray[x1+diff][y1-diff] = lineArray[x1+diff][y1-diff] + 1
                    count = count + 1
                    break

                if y1 < y2:
                    print(line)
                    for i in range(y1, y2+1):
                        diff = i - y1
                        print(x1+diff)
                        print(i)
                        lineArray[x1+diff][i] = lineArray[x1+diff][i] + 1      
                    count = count + 1
                    break   
    

f.close()

print('count', count)   

np.set_printoptions(threshold=np.inf)
print(lineArray)

count = np.count_nonzero(lineArray > 1)
print("Total lines cross more than 1 time: ", count)

## consider only cases where x=x2 or y1-y2

## create empty numpy array of 10 by 10 

##for each pair that create a line

# check is x or y differs

# start at starting point and 