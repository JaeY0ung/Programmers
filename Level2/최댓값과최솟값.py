# def solution(s):
#     arr1 = s.split()
#     arr2 = []
#     for i in arr1:
#         arr2.append(int(i))
#     return str(min(arr2)) + " " + str(max(arr2))
# print(solution("1 2 3 4"))




# def solution(s):
#     arr = [ int(i) for i in s.split()]
#     return str(min(arr)) + " " + str(max(arr))
# print(solution("1 2 3 4"))




# def solution(s):
#     return str(min([int(i) for i in s.split()])) + " " + str(max([int(i) for i in s.split()]))




def solution(s):
    arr = list(map(int, s.split()))
    return str(min(arr)) + " " + str(max(arr))
print(solution("1 2 3 4"))