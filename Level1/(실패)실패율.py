# def solution(N, stages):
#     # total = len(stages) # total : 유저 수
#     arr = [[] for _ in range(N)]    # list1: [ [],...,[] ]
#     for i in range(1, N+1): # i : 스테이지
#         nonClearNum = 0   # 스테이지 도달한 사람 중 머물러 있는 사람.
#         totalNum = 0   # 스테이지 도달한 사람 
#         for ppl in stages: 
#             if ppl == i:
#                 totalNum += 1
#                 nonClearNum += 1
#             if ppl > i:
#                 totalNum += 1
        
#         arr[i-1].append(i)
#         arr[i-1].append(round(nonClearNum / totalNum, 6))
#     print(arr)
#     arr.sort(key = lambda x:x[1], reverse = True)
#     list2 = []
#     for l in range(len(arr)):
#         list2.append(arr[l][0])
#     return list2

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	))

# def solution(N, stages):            # 5, [2, 1, 2, 6, 2, 4, 3, 3] 입력
#     arr1 = [[_ + 1] for _ in range(N)] # [[1], [2], [3], [4], [5]]
#     sorted_arr = sorted(stages)     # [1,2,2,2,3,3,4,6]
#     total = len(stages)             # total : 8
#     for j in range(2, N + 2):   # j: 2 ~ N + 1 
#         for i in range(total):
#             if sorted_arr[i] >= j:  # i번째 수가 처음으로! j일때
#                 p = round( sorted_arr.count(j-1) / (total - i + sorted_arr.count(j-1)), 3)
#                 arr1[j-2].append(p) # 실패율 3자리수까지.
#                 break
#     print(arr1) # [[1, 0.125], [2, 0.429], [3, 0.5], [4], [5, 0.0]]
#     arr1 = sorted(arr1, key = lambda x: x[1], reverse = True)
#     print(arr1) # [[3, 0.5], [4, 0.5], [2, 0.429], [1, 0.125], [5, 0.0]]
#     list2 = []
#     for l in range(len(arr1)):
#         list2.append(arr1[l][0])
#     return list2

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))

def solution(N, stages):     #시간 초과는 없음!
    arr1 = [] 
    for i in range(1, N + 2):  # i:  1 ~ n+1
        arr1.append(stages.count(i))

    #print(arr1)    # [1, 3, 2, 1, 0, 1]
    arr2 = []
    for j in range(0, N):  # 0 <= j <= N
        if arr1[j] != 0:
            p = arr1[j]/ sum(arr1[j:])   #라운드 함수 안 사용해도 됨!
        else:
            p = 0
        arr2.append(p)
    print(arr2)   #[0.125, 0.428571, 0.5, 0.5, 0.0]
    result = []
    for _ in range(N):
        for i in range(N):
            if arr2[i] == max(arr2):
                result.append(i+1)
                arr2[i] = -1
                break
    return result
                
                
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))