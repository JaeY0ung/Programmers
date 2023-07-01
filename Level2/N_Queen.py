# import itertools     #1  시간초과

# def solution(n):
#     p1 = list(itertools.permutations([i for i in range(n)], n))
#     result = 0
#     for y in p1:
#         set1 = set()
#         set2 = set()
#         for i in range(n):   # set1, set2 만들기.
#             set1.add(i + y[i])
#             set2.add(i - y[i])
#         if len(set1) == n and len(set2) == n:  
#             result += 1
#     return result



# import itertools   #2 #1보다 시간 덜 초과. 테스트8: 484, 테스트9: 4569
# def solution(n):
#     p1 = list(itertools.permutations([_ for _ in range(n)], n))
#     result = 0
#     for y in p1:
#         set1 = set()
#         set2 = set()
#         isTrue = True
#         for i in range(n):   # set1, set2 만들기.
#             if (i + y[i] in set1) or (i - y[i] in set2):
#                 isTrue = False
#                 break
#             set1.add(i + y[i])
#             set2.add(i - y[i])
            
#         if isTrue == True:
#             result += 1
#     return result


import itertools       #3  테스트8: 252, 테스트9: 2638   테스트1: 실패
from math import factorial
def solution(n):  
    if n == 1:
        return 1
    p1 = list(itertools.permutations([_ for _ in range(n)], n))
    num = factorial(n)
    result = 0
    for y in p1[0:num//2]:
        set1 = set()
        set2 = set()
        isTrue = True
        for i in range(n):   # set1, set2 만들기.
            if (i + y[i] in set1) or (i - y[i] in set2):
                isTrue = False
                break
            set1.add(i + y[i])
            set2.add(i - y[i])
            
        if isTrue == True:
            result += 1
    return result * 2



# import itertools   #(#2 기반 코드)
# def solution(n):
#     p1 = list(itertools.permutations([_ for _ in range(n)], n))
#     print(p1)
#     result = 0
#     for y in p1:
#         set1 = set()
#         set2 = set()
#         isTrue = True
#         for i in range(n):   # set1, set2 만들기.
#             if (i + y[i] in set1) or (i - y[i] in set2):
#                 isTrue = False
#                 break
#             set1.add(i + y[i])
#             set2.add(i - y[i])
#         if isTrue == True:
#             result += 1
#     return result

print(solution(4))