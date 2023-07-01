# def solution(scoville, K):   # 테스트 전부 통과, 효율성테스트 전부 시간초과 실패.
#     try:
#         count = 0
#         scoville.sort()
#         while scoville[0] < K:
#             a = scoville[0] + scoville[1] * 2
#             del scoville[0]
#             scoville[0] = a
#             count += 1
#             scoville.sort()
#         return count
#     except:
#         return -1



# def solution(scoville, K):
#     count = 0
#     # scoville.sort()
#     while True :
#         # 새로운 요리 만들기
#         a = scoville[0] + scoville[1] * 2
#         del scoville[0:2]
#         # sort 과정
#         if a >= scoville[-1]:   
#                 scoville.append(a)
#         else:
#             for i in range(len(scoville)):
#                 if a < scoville[i]:
#                     scoville.insert(i, a)
#                     break
#         count += 1
#         if scoville[0] >= K:
#             return count
#         else:
#             if len(scoville) == 1:
#                 return -1





def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True :
        # 새로운 요리 만들기
        a = scoville[0] + scoville[1] * 2
        del scoville[0]
        scoville[0] = a
        # sort 과정
        scoville.sort()
        answer += 1
        print(scoville)
        if scoville[0] >= K:
            return answer
        else:
            if len(scoville) == 1:
                return -1


print(solution([1, 2, 3, 9, 10, 12], 7))