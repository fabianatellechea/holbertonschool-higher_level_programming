#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    mul = 0
    average = 0
    add = 0
    for i in my_list:
        mul += i[0] * i[1]
        add += i[1]
        average = mul / add
    return average
