from math import ceil
import copy
def solution(progresses, speeds):
    arr1 = []
    l = len(progresses)
    maxNum = 0

    for i in range(l):
        a = progresses[i]
        b = speeds[i]
        maxNum = max( maxNum, ceil((100 - a) / b ) )
        arr1.append( maxNum )    # [5, 10, 1, 1, 20, 1]   -->  [5, 10, 10, 10, 20, 20]

    arr2 = copy.deepcopy(arr1)
    arr2 = list(dict.fromkeys(arr2))
    arr3 = []
    for things in arr2:
        arr3.append(arr1.count(things))
    print(arr3)

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))