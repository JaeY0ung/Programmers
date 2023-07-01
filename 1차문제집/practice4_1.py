import copy
from operator import xor
def solution(beginning, target):
    l = len(beginning)
    count = 0
    count2 = 0
    oxList = [[] for _ in range(l)]
    for i in range(l):    # 같으면 0 다르면 1
        for j in range(l):
            oxList[i].append(beginning[i][j] ^ target[i][j])

    oxList2 = copy.deepcopy(oxList)  #하나 더 생성

    # print(f"테스트1: {oxList},\n{oxList2}\n")  # 테스트1

    for i in range(l):
        if oxList[i][0] == 1:
            for j in range(l):
                oxList[i][j] = 1- oxList[i][j]
            count += 1
    for j in range(l):
        if oxList[0][j] == 1:
            for i in range(l):
                oxList[i][j] = 1- oxList[i][j]
            count += 1

    print(f"테스트2: {oxList},\n{oxList2}\n")  # 테스트2

    for j in range(l):
        if oxList2[0][j] == 1:
            for i in range(l):
                oxList2[i][j] = 1- oxList2[i][j]
            count2 += 1
    for i in range(l):
        if oxList2[i][0] == 1:
            for j in range(l):
                oxList2[i][j] = 1- oxList2[i][j]
            count2 += 1
    
    minCount = 15
    if oxList == [[0 for __ in range(l)] for _ in range(l)]:
        minCount = count
    if oxList2 == [[0 for __ in range(l)] for _ in range(l)]:
        minCount = min(minCount, count2)
    if minCount == 15:
        return -1
    else:
        return minCount
    




print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], \
    [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],\
     [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], \
        [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
