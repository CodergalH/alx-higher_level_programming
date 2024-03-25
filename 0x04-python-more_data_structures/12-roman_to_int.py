#!/usr/bin/python3
def roman_to_int(roman_string):
    romanum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if isinstance(roman_string, str):
        str_list = list(roman_string)
        num = 0

        for i in range(len(str_list)):
            place = romanum[str_list[i]]

            if i + 1 < len(str_list) - 1 or i + 1 == len(str_list) - 1:
                nextp = romanum[str_list[i + 1]]

                if place < nextp:
                    place = nextp - place
                    i += 2

            num += place

        return num
    else:
        return 0
