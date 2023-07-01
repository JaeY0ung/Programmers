# def solution(arr):         # [1,1,3,3,0,1,1]
#     l = len(arr)
#     # count = 0
#     list_1 = []
    
#     for i in range(l - 1):      # [-1,1,-1,3,0,-1,1]   -1 로 바꾸어버리기.
#         if arr[i] == arr[i + 1]:
#             arr[i] = -1
#             # count += 1
#             list_1.append(i)    # list에 -1 인 순번 저장.
#     # for _ in range(count):
#     #     arr.remove(-1)
    
#     count_1 = 0
#     for j in list_1:
#         i = j - count_1
#         del arr[i]
#         count_1 += 1
            
#     return arr

# def solution(arr):
#     l = len(arr) - 1
#     list_1 = []
#     count_1 = 0

#     for i in range(l):
#         if arr[i] == arr[i + 1]:
#             list_1.append(i)

#     for j in list_1:
#         del arr[j - count_1]
#         count_1 += 1
            
#     return arr



# def solution(arr):
#     i = 0
#     count = 0
#     while count <= len(arr) - 1 :
#         if arr[i] == arr[i + 1]:
#             del arr[i]
#         else:
#             i += 1
#         count += 1

#     return arr

# def solution(arr):      # 효율성 테스트 통과 X
#     i = 0
#     while i < len(arr) - 1 :
#         if arr[i] == arr[i+1]:
#             del arr[i]
#             continue
#         else:
#             i += 1
#     return arr
# print(solution([1,1,3,3,0,1,1]))



def solution(arr):
    l = len(arr)
    j = 0
    list1 = []
    for i in range(l-1):
        if arr[i] != arr[i+1]:
            list1.append(arr[j:i+1])
            j = i + 1
    list1.append(arr[j:])
    list2 = []
    for li in list1:
        list2.append(li[0])
    return list2
print(solution([1,1,3,3,0,1,1]))
            