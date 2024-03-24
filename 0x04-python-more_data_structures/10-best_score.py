#!/usr/bin/python3
def best_score(a_dictionary):
    newlist = list(a_dictionary)
    for i in range(len(newlist)):
        for x in range(i):
            if a_dictionary[newlist[i]] > a_dictionary[newlist[x]]:
                temp = a_dictionary[newlist[i]]
                a_dictionary[newlist[i]] = a_dictionary[newlist[x]]
                a_dictionary[newlist[x]] = temp

    newlist = list(a_dictionary)
    return a_dictionary[newlist[0]]
