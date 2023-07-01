# def solution(n):
#     if n == 1 or n == 2:
#         return 1
#     return solution(n-1) + solution(n-2)

def solution(n):
    a = 0
    b = 1   # F(2) 구하기.
    for i in range(n-1):
        c = b % 1234567
        b = (b + a) %1234567
        a = c
    #print(b)
    return b

print(solution(10000))

        





    