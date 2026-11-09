def bubbleSort(lst):
    repeat = True
    while repeat:
        repeat = False
        for i in range(len(lst) - 1):
            if lst[i + 1] > lst[i]:
                temp1 = lst.pop(i)
                temp2 = lst.pop(i)
                lst.insert(i, temp1)
                lst.insert(i, temp2)
                repeat = True
    return lst
from random import shuffle
def randomSort(lst):
    repeat = True
    while repeat:
        repeat = False
        for i in range(len(lst) - 1):
            if lst[i + 1] > lst[i]:
                repeat = True
        if repeat:
            lst = shuffle(lst)
    return lst
import math
def binarySearch(value, lst):
    if value in lst:
        while len(lst) > 1:
            if value > lst[math.floor(len(lst) / 2)]:
                lst = lst[math.floor(len(lst) / 2):len(lst)]
            else:
                lst = lst[0:math.ceil(len(lst) / 2)]
        return lst[0]
    else:
        raise Exception