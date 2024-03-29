#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    for i in range(len(roman_string)):
        j = i - 1
        if i > 0 and roman[roman_string[i]] > roman[roman_string[j]]:
            res += roman[roman_string[i]] - 2 * roman[roman_string[j]]
        else:
            res += roman[roman_string[i]]

    return res
