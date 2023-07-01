# from itertools import permutations               # 시간초과
# def solution(numbers):   # [6, 10, 2]
#     l = len(numbers)
#     set1 = set(permutations(numbers, l))
#     set2 = set()

#     for arr in set1:
#         sum = ''
#         for arr1 in arr:
#             sum += str(arr1)
#         set2.add(int(sum))
#     return str(max(set2))

# print(solution([6, 10, 2]))


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# from itertools import permutations                # 시간초과
# def solution(numbers):   # [6, 10, 2]
#     l = len(numbers)
#     set1 = list(set(permutations(numbers, l)))
#     # print(set1)
#     maxNum = 0
#     for i in range(len(set1)):
#         sumstr = ''
        
#         for arr1 in set1[i]:
#             sumstr += str(arr1)
#             sumint = int(sumstr)

#         if sumint > maxNum:
#             maxNum = sumint
#         print(maxNum)

#     return str(maxNum)
# print(sorted([str(k) for k in range(100)]))



# def solution(numbers):
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     arr4 = []
#     for num in numbers:
#         if len(num) == 1:
#             arr1.append(num)
#         elif len(num) == 2:
#             arr2.append(num)
#         elif len(num) == 3:
#             arr3.append(num)
#         elif len(num) == 4:
#             arr4.append(num)
#     arr1.sort()
#     arr2.sort()
#     arr3.sort()
#     arr4.sort()
#     arr1 = arr1[::-1]
#     arr2 = arr2[::-1] 
#     arr3 = arr3[::-1] 
#     arr4 = arr4[::-1] 

# print(solution([3, 30, 34, 5, 9]))


# from itertools import permutations


# def solution(numbers):   # [6, 10, 2]
#     l = len(numbers)
#     set1 = list(permutations(numbers, l))
#     maxNum = 0
#     array = []
    
#     for i in range(len(set1)):
#         sumstr = ''
#         for arr1 in set1[i]:
#             sumstr += str(arr1)
#         array.append(int(sumstr))
#     return str(max(array))


from itertools import permutations    # 1~6 시간초과  11 시간초과

def solution(numbers):   # [6, 10, 2]
    answer = ''
    arr0 = []
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    arr5 = []
    arr6 = []
    arr7 = []
    arr8 = []
    arr9 = []
    numbers = [str(i) for i in numbers]
    for num in numbers:
        
        if num[0] == '0':
            arr0.append(num)
        elif num[0] == '1':
            arr1.append(num)
        elif num[0] == '2':
            arr2.append(num)
        elif num[0] == '3':
            arr3.append(num)
        elif num[0] == '4':
            arr4.append(num)
        elif num[0] == '5':
            arr5.append(num)
        elif num[0] == '6':
            arr6.append(num)
        elif num[0] == '7':
            arr7.append(num)
        elif num[0] == '8':
            arr8.append(num)
        elif num[0] == '9':
            arr9.append(num)
    # arr0.sort()
    # arr1.sort()
    # arr2.sort()
    # arr3.sort()
    # arr4.sort()
    # arr5.sort()
    # arr6.sort()
    # arr7.sort()
    # arr8.sort()
    # arr9.sort()
    # arr0 = arr0[::-1]
    # arr1 = arr1[::-1]
    # arr2 = arr2[::-1]
    # arr3 = arr3[::-1]
    # arr4 = arr4[::-1]
    # arr5 = arr5[::-1]
    # arr6 = arr6[::-1]
    # arr7 = arr7[::-1]
    # arr8 = arr8[::-1]
    # arr9 = arr9[::-1]

    if len(arr9) != 0:
        arr9 = [int(i) for i in list(map(''.join, permutations(arr9)))]
        answer += str(max(arr9))
    if len(arr8) != 0:
        arr8 = [int(i) for i in list(map(''.join, permutations(arr8)))]
        answer += str(max(arr8))
    if len(arr7) != 0:
        arr7 = [int(i) for i in list(map(''.join, permutations(arr7)))]
        answer += str(max(arr7))
    if len(arr6) != 0:
        arr6 = [int(i) for i in list(map(''.join, permutations(arr6)))]
        answer += str(max(arr6))
    if len(arr5) != 0:
        arr5 = [int(i) for i in list(map(''.join, permutations(arr5)))]
        answer += str(max(arr5))
    if len(arr4) != 0:
        arr4 = [int(i) for i in list(map(''.join, permutations(arr4)))]
        answer += str(max(arr4))
    if len(arr3) != 0:
        arr3 = [int(i) for i in list(map(''.join, permutations(arr3)))]
        answer += str(max(arr3))
    if len(arr2) != 0:
        arr2 = [int(i) for i in list(map(''.join, permutations(arr2)))]
        answer += str(max(arr2))
    if len(arr1) != 0:
        arr1 = [int(i) for i in list(map(''.join, permutations(arr1)))]
        answer += str(max(arr1))
    if len(arr0) != 0:
        arr0 = [int(i) for i in list(map(''.join, permutations(arr0)))]
        answer += str(max(arr0))

    return answer
    
print(solution([3, 30, 34, 5, 9]))
      
