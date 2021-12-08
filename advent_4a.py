from typing import final
import numpy as np 

# read in the document
with open('/Users/sinievanderben/Documents/advent/advent_data3.txt', 'r') as f:
    lines = f.readlines()

    newArray = False
    count = 0 
    bingolist = []

    for line in lines:
        if count == 0:
            bingo_numbers = line.split(',') 
            count = count + 1
        else:
            if len(line.strip()) == 0:
                if newArray == True:
                    newArray = False
                    bingolist.append(bingoArray)
                count = count +1
            else:
                if newArray == False:

                    bingoArray = np.empty((5,5))
                    newArray = True
                    bingoCount = 0
                    for i in range(5):
                        bingoArray[bingoCount][i] = int(line.split()[i])
                else:
                    bingoCount = bingoCount + 1
                    for i in range(5):
                        bingoArray[bingoCount][i] = int(line.split()[i])

f.close()

final_number = 0 
final_list = []
keep_final = True 

for number in bingo_numbers:
    if keep_final:
        for card in range(len(bingolist)):
            
            # Set to 0 when number is found 
            bingolist[card][bingolist[card] == int(number)] = 0

            for row in bingolist[card]:
                    
                if np.sum(row) == 0:
                    print('yes')
                    final_number = number
                    final_list.append(bingolist[card])
                    keep_final = False

            for column in range(5):
                if np.sum(bingolist[card][:,column]) == 0:
                    final_number = number
                    final_list.append(bingolist[card])
                    keep_final = False
    else:
        break

print("final number: ", final_number)
print("final card:", final_list[0])
print(len(final_list))

total_sum = 0 
for final_row in final_list[0]:
    total_sum = total_sum + sum(final_row)

print(total_sum * int(final_number))
