from math import comb as c
def solution(n):
#     def fac(x):
#         if x <= 1:
#             return 1
#         return fac(x-1) * x
#     def comb(n,r):
#         return fac(n) / fac(r) // fac(n-r) 
    sum = 0
    for i in range(n//2 +1):
        sum += c(n-i,i) % 1234567
        sum %= 1234567
    return sum