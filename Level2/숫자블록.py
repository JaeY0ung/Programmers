# def solution(begin, end):
#     arr = [ i for i in range(begin, end+1)]
#     result = []
#     for n in arr:
#         if n == 1:
#             result.append(0)
#         elif n == 2 or n == 3:
#             result.append(1)
#         elif n >= 4:
#             isTrue = True
#             for i in range(2,int(n**(0.5))+1):
#                 if n % i == 0:
#                     result.append(n//i)
#                     isTrue = False
#                     break
#             if isTrue == True:
#                 result.append(1)
#     return result


# def solution(begin, end):
#     arr = [ i for i in range(begin, end+1)]
#     result = []
#     for n in arr:
#         if n == 1:
#             result.append(0)
#         elif n == 2 or n == 3:
#             result.append(1)
#         else:
#             isTrue = True
#             for i in range(2,int(n**(0.5))+1):
#                 if n % i == 0:
#                     result.append(n//i)
#                     isTrue = False
#                     break
#             if isTrue == True:
#                 result.append(1)
#     return result


def solution(begin, end):
    arr = [ i for i in range(begin, end+1)]
    result = []
    for n in arr:
        if n == 1:
            result.append(0)
        elif n == 2 or n == 3:
            result.append(1)
        else:
            isTrue = True
            for i in range(2,int(n**(0.5))+1):
                if n % i == 0:
                    if n//i <= 10000000:
                        result.append(n//i)
                        isTrue = False
                        break
                    else:
                        continue
            if isTrue == True:
                result.append(1)
    return result