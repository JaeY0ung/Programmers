# from math import ceil   # 답은 맞았지만 효율성 테스트 통과 x
# def solution(n, works):
#     mysum = sum(works)
#     l = len(works)
#     works = sorted(works, reverse = True)
#     if mysum <= n:
#         return 0
#     i = 0
#     while True:
#         if i == l - 1:
#             i = 0
#         if works[i] > works[i+1]:
#             works[i] -= 1
#             n -= 1
#             i = 0
#         else:
#             i += 1
#         if n == 0 :
#             break
#         result = True
#         for j in range(l):
#             if works[j] != works[0]:
#                 result = False
#                 break
#         if result == True:
#             a = n // l # 최소 빼는 수
#             b = ceil(n / l) # 최대 빼는 수
#             c = n % l # b 빼는 횟수.
#             for i in range(l):
#                 if 0 <= i < c:
#                     works[i] -= b
#                 else:
#                     works[i] -= a
#             break
#     answer = 0
#     for num in works:
#         answer += num ** 2
#     return answer





# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (32.01ms, 10.2MB)
# 테스트 9 〉	통과 (145.09ms, 10.2MB)
# 테스트 10 〉통과 (0.02ms, 10.4MB)
# 테스트 11 〉통과 (0.01ms, 10.3MB)
# 테스트 12 〉통과 (0.03ms, 10.3MB)
# 테스트 13 〉통과 (0.00ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)





# from math import ceil   # 훨씬 빨라지긴했음 (약 70배까지도?) 그래도 아직 부족.

# def solution(n, works):
#     mysum = sum(works)
#     l = len(works)
#     works = sorted(works, reverse = True)
#     if mysum <= n:
#         return 0
#     i = 0
#     while True:
#         if i == l - 1:
#             result = True
#             for j in range(l):
#                 if works[j] != works[0]:
#                     result = False
#                     break
#             if result == True:
    #             a = n // l # 최소 빼는 수
    #             b = ceil(n / l) # 최대 빼는 수
    #             c = n % l # b 빼는 횟수.
    #             for i in range(l):
    #                 if 0 <= i < c:
    #                     works[i] -= b
    #                 else:
    #                     works[i] -= a
    #             break
    #         i = 0
            
    #     if works[i] > works[i+1]:
    #         works[i] -= 1
    #         n -= 1
    #         i = 0
    #     else:
    #         i += 1
    #     if n == 0 :
    #         break
    # answer = 0
    # for num in works:
    #     answer += num ** 2
    # return answer

# 테스트 1 〉 통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.51ms, 10.4MB)
# 테스트 9 〉	통과 (2.09ms, 10.3MB)
# 테스트 10 〉통과 (0.02ms, 10.3MB)
# 테스트 11 〉통과 (0.01ms, 10.4MB)
# 테스트 12 〉통과 (0.02ms, 10.2MB)
# 테스트 13 〉통과 (0.00ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)

from math import ceil


def solution(n, works):
    mysum = sum(works)
    l = len(works)
    works = sorted(works, reverse = True)
    if mysum <= n:
        return 0
    else:
        i = 0
        while True:
            if works[i] > works[i+1]:
                if works[i] - works[i+1] <= n:
                    works[i] = works[i+1]
                    n -= works[i] - works[i+1]
                    i = 0
                else:
                    works[i] -= n
                    n = 0
            else:
                i += 1
            if n == 0:
                answer = 0
                for num in works:
                    answer += num ** 2
                    print(works)
                return answer

            if i == l - 1:
                a = n // l # 최소 빼는 수
                b = ceil(n / l) # 최대 빼는 수
                c = n % l # b 빼는 횟수.
                for i in range(l):
                    if 0 <= i < c:
                        works[i] -= b
                    else:
                        works[i] -= a
                answer = 0
                for num in works:
                    answer += num ** 2
                    print(works)
                return answer
        

print(solution(4, [4,3,3]))
