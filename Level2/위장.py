# from itertools import combinations as c
# from functools import reduce
# def solution(clothes):
#     arrType = []
#     arrNum = []
#     listComb = []
#     for x in clothes:
#         if x[1] in arrType:
#             arrNum[arrType.index(x[1])] += 1
#         else:
#             arrType.append(x[1])
#             arrNum.append(1)
#     sum1 = sum(arrNum)
#     for r in range(2,len(arrNum)+1):
#         for t in list(c(arrNum,r)):
#             sum1 += reduce(lambda x, y: x * y, t)
    
#     # print(listComb)
#     return sum1






def solution(clothes):
    arrType = []
    arrNum = []
    for x in clothes:
        if x[1] in arrType:
            arrNum[arrType.index(x[1])] += 1
        else:
            arrType.append(x[1])
            arrNum.append(1)
    num = 1
    for num in arrNum:
        num *= (num + 1)
    num -= 1
    return num



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))