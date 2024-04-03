#!/usr/bin/python3
def roman_to_int(roman_string):
    romanum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str):
        return 0
    
    str_list = list(roman_string)
    num = 0
    lenght = len(str_list) - 1

    for i in range(lenght - 1):
        place = romanum[str_list[i]]
        next = i + 1
        nextp = romanum[str_list[next]]

        if (next < lenght) and (place < nextp):
                place *= -1

        num += place

    return num

