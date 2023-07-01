# from math import *
# def solution(k, d):
#     count = 0
#     r = d/k
#     for i in range(floor(r) + 1):
#         for j in range(floor(r)-i+1, floor(r) + 1):
            
#             if (i)**2 + (j)**2 <= r ** 2:
#                 count += 1
#             else:
#                 break
#     return count + (i+1)*(i+2)//2


# from math import *

# def solution(k, d):
#     count = 0       
#     r = d/k

#     for i in range(floor(r/sqrt(2))+1):
#         for j in range(max(i, floor(r)-i)+1, floor(r) + 1):
#             if (i)**2 + (j)**2 <= r ** 2:
#                 count += 1
#             else:
#                 break

#     return 2 * count + (i+1)*(i+2)//2 + int(r/sqrt(2)) - floor(r)//2



from math import *    # 성공
def solution(k, d):
    count = 0
    r = d/k
    for i in range(floor(r) + 1):
        count += int(r) - int(sqrt(r**2 - i**2))
    return int(r+1)**2 - count