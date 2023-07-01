from math import ceil
def solution(n, left, right):
    arr = [i+1 for i in range(n)]
    k = ceil(right / n)
    for s in range(1, k):
        arr2 = [s+1 for _ in range(s)] + [i+1 for i in range(s, n)]
        arr.extend(arr2)
    return arr[left:right +1]
print(solution(3,2,5))