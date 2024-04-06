#!/usr/bin/python3
def weight_average(my_list=[]):
    if  len(my_list) == 0:
        return 0
    
    total = 0
    for i in range(len(my_list)):
        num = 1
        for j in range(len(my_list[i])):
            num *= my_list[i][j]
        
        total += num

    avg = 0
    for i in range(len(my_list)):
        avg += list(my_list[i]).pop()

    average = total / avg

    return  average
