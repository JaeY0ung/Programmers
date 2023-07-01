from math import sqrt, floor
def solution(n):
    count = 1
    for num in range(3, n+1):
        result = None
        for i in range(2, floor(sqrt(num)) + 1):
            if num % i == 0:
                result = False
                break
        if result != False:
            count += 1
    return count