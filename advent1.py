import numpy as np

### divide into parts of 3
with open('/Users/sinievanderben/Documents/advent/data_advent1.txt', 'r') as f:
    lines = f.readlines()
    numLines = len(lines)%3

    count = 0 # to keep track of total numbers
    countIncreased = 0 # to keep trac of increased
    prevNumber = 0 # to keep track of previous number for comparison 

    while count!=(len(lines)-numLines):
        number = int(lines[count]) + int(lines[count+1]) + int(lines[count+2])

        if count > 0:
            if number > prevNumber:
                countIncreased = countIncreased + 1
                print(count, number, "Increased")
            else:
                print(count, number, "Decreased")


        
        prevNumber = number
        count = count + 1
    
    print(countIncreased)

f.close()

### compare A with B

### compare B with C

### compare previous window with next window


