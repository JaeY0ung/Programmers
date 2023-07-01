# def solution(number, k):   # 태스트 8 10 12 통과 못함.
#     count = k
#     while count != 0:
#         for i in range(len(number)-1):
#             if int(number[i]) < int(number[i+1]):
#                 number = number[:i] + number[i+1:]
#                 count -= 1
#                 break
#     return number


