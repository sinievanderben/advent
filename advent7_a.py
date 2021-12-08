
# horizontal position of each crab


# each change of 1 step in horizontal position of a single crab takes 1 fuel

# determine the least fuel posiion 

import numpy as np 
import math
        

with open('/Users/sinievanderben/Documents/advent/test_day7.txt', 'r') as f:
    lines = f.readlines()
    splitted_lines = lines[0].split(',')

    splitted_numbers = [int(x) for x in splitted_lines]

    max_fuel = math.inf
    best_fuel = 0

    for fuel in range(max(splitted_numbers)):
        fuel_temp = 0 
        for number in splitted_numbers:
            for steps in range(abs(fuel-number)+1):
                fuel_temp = fuel_temp + steps
        
        if fuel_temp < max_fuel:
            max_fuel = fuel_temp
            best_fuel = fuel
    
    print(max_fuel)
    print(best_fuel)

