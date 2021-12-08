# exponential

# 1 fish creates a new fish every 7 days

# model a fish as a unit of days until it creates another fish

# new fish gets 2 days extra

# create a list of the input


## Line segements 1 --> line segments 2
import numpy as np 
        

with open('/Users/sinievanderben/Documents/advent/advent_day6.txt', 'r') as f:
    lines = f.readlines()
    splitted_lines = lines[0].split(',')

    state0 = 0
    state1 = 0
    state2 = 0
    state3 = 0
    state4 = 0
    state5 = 0
    state6 = 0
    state7= 0 
    state8 = 0

    for i in range(len(lines[0].split(','))):
        if int(splitted_lines[i]) == 0:
            state0 = state0 + 1
        if int(splitted_lines[i]) == 1:
            state1 = state1+ 1
        if int(splitted_lines[i])  == 2:
            state2 = state2 + 1
        if int(splitted_lines[i])  == 3:
            state3 = state3 + 1
        if int(splitted_lines[i]) == 4:
            state4 = state4 + 1
        if int(splitted_lines[i])  == 5:
            state5 = state5 + 1
        if int(splitted_lines[i]) == 6:
            state6 = state6 + 1
        if int(splitted_lines[i])  == 7:
            state7 = state7 + 1
        if int(splitted_lines[i])  == 0:
            state8 = state8 + 1
    
    days = 256
    
    for day in range(days):
        print('day', day)
        print(state0 + state1 + state2+ state3 + state4 + state5 + state6 + state7+ state8)
        

        print(state0)
        print(state1)
        print(state2)
        print(state3)
        print(state4)
        print(state5)
        print(state6)
        print(state7)
        print(state8)

        newfish = state0
        
        state0 = state1
        state1 = state2
        state2 = state3
        state3 = state4
        state4 = state5
        state5 = state6
        state6 = state7 + newfish
        state7 = state8
        state8 = newfish


final_fish = state0 + state1 + state2+ state3 + state4 + state5 + state6 + state7+ state8
print(final_fish)