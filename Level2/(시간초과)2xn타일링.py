# from math import comb
# def solution(n):
#     sum = 0
#     for k in range(n//2 +1):
#         sum += comb(n-k, k)
#     if sum > 1000000007:
#         sum %= 1000000007
#     return sum
# print(solution(4))


# from math import comb
# def solution(n):
#     sum = 0
#     for k in range(n//2 +1):
#         sum += comb(n-k, k)
#         if sum > 1000000007:
#             sum %= 1000000007
#     return sum
# print(solution(4))

def solution(n):
    sum = 0
    for k in range(n//2 + 1):
        com = 1
        if k < n//3:
            for i in range(n-2*k+1, n-k+1):
                com *= i
            for j in range(2, k+1):
                com /= i
        else:
            for i in range(k+1, n-k+1):
                com *= i
            for j in range(2, n-2*k+1):
                com /= j
        sum += com
        sum %= 1000000007
    return int(sum)
print(solution(4))