from collections import deque

def solution(queue1, queue2):    # 22 23 24 시간초과
    count = 0
    l = len(queue1) * 3      # 이게 중요!!!
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while True:
        # if count == l or num1 == 0 or num1 == len(queue1):
        if count == l:
            break
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1[0])
            queue1.popleft()
            count += 1
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2[0])
            queue2.popleft()
            count += 1
        else:
            break
    if sum1 == sum2:
        return count
    else:
        return -1



# def solution(queue1, queue2):
#     sum1 = sum(queue1)
#     l = len(queue1)
#     avg12 = (sum(queue1) + sum(queue2)) // 2 
#     i = 0
#     j = 0
#     count = 0
#     while True:
#         if sum1 == avg12:
#             break

#         elif count == 2 * l:
#             break

#         elif sum1 > avg12:
#             if i == l:
#                 break
#             sum1 -= queue1[i]
#             i += 1
#             count += 1

#         elif sum1 < avg12:
#             if j == l:
#                 break
#             sum1 += queue2[j]
#             j += 1
#             count += 1

#     if sum1 == avg12:
#         return count
#     else: 
#         return -1
