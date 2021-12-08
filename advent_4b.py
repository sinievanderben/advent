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
        length = len(bingolist)
        alreadyRemoved = 0
        print(length)

        if len(bingolist) == 1:
            bingolist[0][bingolist[0] == int(number)] = 0

            for row in bingolist[0]:
                if len(bingolist) == 0:
                    keep_final = False
                elif np.sum(row) == 0:
                    final_number = number
                    final_list.append(bingolist[0])
                    bingolist.pop(0)
                    keep_final = False

            for column in range(5):
                if len(bingolist) == 0:
                    keep_final = False
                elif np.sum(bingolist[0][:,column]) == 0:
                    final_number = number
                    final_list.append(bingolist[0])
                    bingolist.pop(0)
                    keep_final = False
            

        else: 
            for card in range(length):
                
                # Set to 0 when number is found 
                bingolist[card-alreadyRemoved][bingolist[card-alreadyRemoved] == int(number)] = 0

                for row in bingolist[card-alreadyRemoved]:
                        
                    if np.sum(row) == 0:
                        final_number = number
                        final_list.append(bingolist[card-alreadyRemoved])
                        bingolist.pop(card-alreadyRemoved)
                        alreadyRemoved = alreadyRemoved + 1

                for column in range(5):
                    if np.sum(bingolist[card-alreadyRemoved][:,column]) == 0:
                        final_number = number
                        final_list.append(bingolist[card-alreadyRemoved])
                        bingolist.pop(card-alreadyRemoved)
                        alreadyRemoved = alreadyRemoved + 1
        
    else:
        break

print("final number: ", final_number)
print("final card:", final_list[0])
print(len(final_list))

total_sum = 0 
for final_row in final_list[len(final_list)-1]:
    total_sum = total_sum + sum(final_row)

print(total_sum * int(final_number))
