import numpy as np

# lees de digits die je sws weet

# maak een list of array voor de digit

# lees de digits die je niet direct weeet, afleiden

# lees de digits na de streep

def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

with open('/Users/sinievanderben/Documents/advent/advent_day8.txt', 'r') as f:
    lines = f.readlines()

    count = 0
    final_output = 0

    for line in lines:

        splitted_line = line.split()

        array0 = []
        array1 = []
        array2 = []
        array3 = []
        array4 = []
        array5 = []
        array6 = []
        array7 = []
        array8 = []
        array9 = []

        leftovers = splitted_line[:10]
        
        ## do something with left overs

        
            
        while True:
            if len(leftovers) == 0:
                break
            for leftover in leftovers:

                index = leftovers.index(leftover)

                if len(leftovers) == 0:
                    break

                if len(leftover) == 2:
                    array1 = leftover
                    leftovers.pop(index)
                    break
                if len(leftover) == 3:
                    array7 = leftover
                    leftovers.pop(index)
                    break
                if len(leftover) == 7:
                    array8 = leftover
                    leftovers.pop(index)
                    break
                if len(leftover) == 4:
                    array4 = leftover
                    leftovers.pop(index)
                    break


                difference4 = set(array4).symmetric_difference(set(leftover))

                if len((list(difference4))) == 2 and len(leftover) == 6:
                    print("yes 9")
                    array9= leftover
                    leftovers.pop(index)
                    break
                
                difference9 = set(array9).symmetric_difference(set(leftover))

                difference5 = set(array5).symmetric_difference(set(leftover))
                
                # 5 verschilt 1 van de digits van 1 met 9
                if len(difference9) == 1 and len(difference5) == 2:
                    print('yes 3')
                    array3 = leftover
                    leftovers.pop(index)
                    break
                
                difference8 = set(array8).symmetric_difference(set(leftover))

                if len(array1):
                    # it is 6 if it differs 1 from 8 using a number from digit 1
                    if len(list(difference8)) == 1 and (list(difference8).pop(0) == array1[0] or list(difference8).pop(0) == array1[1]):
                        print("yes 6")
                        array6 = leftover
                        leftovers.pop(index)
                        break
                
                difference6 = set(array6).symmetric_difference(set(leftover))

                # 5 verschilt 1 van de digits van 1 met 6
                if len(difference6) == 1:
                    print('yes 5')
                    array5 = leftover
                    leftovers.pop(index)
                    break
                
                # It is zer0 if it differs 1 from 8 and 9 and 6 are already filled 
                if len(list(difference8)) == 1 and array9 and array6:
                    print("yes 0")
                    array0 = leftover
                    leftovers.pop(index)
                    break
                
                if len(leftovers) == 1:
                    print("yes 2")
                    array2 = leftover
                    leftovers.pop(index)
                    break
            
        final_digit = ""
        
        for output in splitted_line[11:]:

            if check_if_equal(output, array0):
                final_digit = final_digit + '0'

            if check_if_equal(output, array1):
                final_digit = final_digit + '1'

            if check_if_equal(output, array2):
                final_digit = final_digit + '2'

            if check_if_equal(output, array3):
                final_digit = final_digit + '3'

            if check_if_equal(output, array4):
                final_digit = final_digit + '4'

            if check_if_equal(output, array5):
                final_digit = final_digit + '5'

            if check_if_equal(output, array6):
                final_digit = final_digit + '6'

            if check_if_equal(output, array7):
                final_digit = final_digit + '7'

            if check_if_equal(output, array8):
                final_digit = final_digit + '8'

            if check_if_equal(output, array9):
                final_digit = final_digit + '9'
        
        print(final_digit)
        
        final_output = final_output + int(final_digit)
print(final_output)


