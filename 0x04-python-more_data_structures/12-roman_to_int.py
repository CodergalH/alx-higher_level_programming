#!/usr/bin/python3
def roman_to_int(roman_string):
    romanum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if isinstance(roman_string, str):
        str_list = list(roman_string)
        num = 0
        lenght = len(str_list) - 1

        for i in range(lenght + 1):
            place = romanum[str_list[i]]
            next = i + 1

            if (next < lenght) or (next == lenght):
                if place < nextp:
                    nextp = romanum[str_list[next]]
                    place = nextp - place
                    i += 1

            num += place

        return num
    else:
        return 0
