import numpy as np

# Set some initial values
horizontal = 0 
depth = 0
aim = 0 


with open('/Users/sinievanderben/Documents/advent/advent_day2.txt', 'r') as f:
    lines = f.readlines()


    for line in lines:
        splitted_lines = line.split(' ')

        if splitted_lines[0] == "forward":
            horizontal = horizontal + int(splitted_lines[1])
            depth = depth + (int(splitted_lines[1])* aim)
        
        if splitted_lines[0] == "down":
            aim = aim + int(splitted_lines[1])
        
        if splitted_lines[0] == "up":
            aim = aim - int(splitted_lines[1])

f.close()

print("horizontal: ", horizontal)
print("depth: ", depth)
final_nuber = depth * horizontal
print("final: ", final_nuber)