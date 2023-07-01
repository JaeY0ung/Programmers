def solution(n, k):
    arr1 = [i for i in range(1,n+1)]
    def fac(num):
        if num <= 1:
            return  1
        return num * fac(num-1)
    arr = []
    k -= 1
    for x in range(1,n+1):   # x: 0 ~ n
        s = k // fac(n - x)
        k = k % fac(n-x)
        arr.append(arr1[s])
        del arr1[s]
    return arr