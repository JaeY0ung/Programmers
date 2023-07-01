from collections import deque as dq

def isRight(array):
    my_array = ''
    for gyalho in array:
        my_array += gyalho
        if '{}' in my_array or '[]' in my_array or '()' in my_array:
            my_array = my_array[:-2]
    if my_array == '':
        return True

def solution(s):
    answer = 0
    l = len(s)
    for i in range(l):
        if i == 0:
            my_arr = s
        else:
            my_arr = s
            my_arr += my_arr[:i]
            my_arr = my_arr[i:]
        if isRight(my_arr) == True:
            answer += 1
        print(my_arr, isRight(my_arr))
    return answer

print(solution("}]()[{"))