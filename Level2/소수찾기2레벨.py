from itertools import permutations

def find(num):   # True 면 소수임.
    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    else:
        result = True
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
        if result == True:
            return True


# def solution(numbers):    #"011"
#     list1 = []
#     for j in range(1, len(numbers) + 1):
#         arr1 = list(set(permutations(numbers, j)))   # 중복제거
#         print(arr1)
#         for arr2 in arr1:
#             sum_arr = ""
#             for arr3 in arr2:
#                 sum_arr += arr3

#             if find(int(sum_arr)) == True:
#                 list1.append(int(sum_arr))
#                 list1 = list(set(list1))
#     print (list1)
#     return len(list1)

def solution(numbers):    #"011"
    set1 = {}
    for j in range(1, len(numbers) + 1):
        set1 = set(permutations(numbers, j))
        print(set1)
        for arr2 in set1:
            sum_arr = ""
            for set3 in arr2:
                sum_arr += set3

            if find(int(sum_arr)) == True:
                set1.add( int(sum_arr) )
    print (set1)
    return len(set1)

print(solution("011"))