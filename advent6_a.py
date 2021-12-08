# exponential

# 1 fish creates a new fish every 7 days

# model a fish as a unit of days until it creates another fish

# new fish gets 2 days extra

# create a list of the input


## Line segements 1 --> line segments 2
import numpy as np 
import time

# read in the document
def createfish(fish_list, untilEighty, day):
    while untilEighty:
        print(day)

        newFish = 0 

        start_time = time.time()

            # Go over current fish 
        for fish in range(len(fish_list)):
                # If current day is 0, append 1 to new fish and reset to 6
            if fish_list[fish] == 0:
                newFish = newFish + 1
                fish_list[fish] = 6
            else:
                    # Take 1 of the current day 
                fish_list[fish] = fish_list[fish] - 1

            # Append new fish 
        for babyfish in range(newFish):
            fish_list.append(8)

        print("One round took ", (time.time()-start_time))

        if day == 255:
            untilEighty = False
            
        day = day + 1

with open('/Users/sinievanderben/Documents/advent/advent_day6.txt', 'r') as f:
    lines = f.readlines()
    splitted_lines = lines[0].split(',')

    fish_list = []
    untilEighty = True
    day = 0 

    for i in range(len(lines[0].split(','))):
        fish_list.append(int(splitted_lines[i]))

    createfish(fish_list, untilEighty, day)

f.close()
print("Number of fish after 256 days: ", len(fish_list))





# go over each element of the list 

# if one is 0, add a fish to the end (do so for every 0 element in the end)
# reset that 6 to 0. 