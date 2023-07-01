from math import ceil
# 1:1  2:1  3:2  4:2
def solution(n,a,b):
    count = 0
    while True:
        a = ceil(a/2)
        b = ceil(b/2)
        count  += 1
        if a == b :
            break
    return count