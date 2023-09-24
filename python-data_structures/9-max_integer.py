#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        for i in my_list:
            maxx = i
            for j in my_list:
                if i < j:
                    maxx = j

                    return maxx
    return None
