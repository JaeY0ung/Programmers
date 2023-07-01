from math import floor


def solution(array, commands):
    list = []
    for _ in range(len(commands)):
        i = commands[_][0]
        j = commands[_][1]
        k = commands[_][2]
        listBeforeSort = array[i-1: j-1]
        listBeforeSort.sort()
        listAfterSort = listBeforeSort
        list.append(listAfterSort[k-1])
    answer = list
    return answer

floor