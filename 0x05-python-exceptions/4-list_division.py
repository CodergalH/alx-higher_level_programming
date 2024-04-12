#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by zero", end="\n")
                result = 0
            except IndexError:
                print("out of range", end="\n")
                result = 0
            except TypeError:
                print("wrong type", end="\n")
                result = 0
            finally:
                new_list.append(result)
    except SyntaxError:
        pass
    finally:
        return(new_list)
    