import numpy as np
import statistics

from statistics import mode 

with open('/Users/sinievanderben/Documents/advent/advent_day3.txt', 'r') as f:
    lines = f.readlines()

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(12):
        number_list = []
        for line in lines:
            number_list.append(line[i])
        
        gamma_rate = gamma_rate + str(mode(number_list))


        if(mode(number_list) == '0'):
            epsilon_rate = epsilon_rate + str(1)
        if(mode(number_list) == '1'):
            epsilon_rate = epsilon_rate + str(0)

eps_int = int(epsilon_rate,2)
gamma_int = int(gamma_rate, 2)

print(eps_int)
print(gamma_int)
print('total: ', eps_int*gamma_int)