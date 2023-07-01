def solution(arr):
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a % b)

    def lcm(a,b):
        return a * b // gcd(a,b)

    k = arr[0]
    for i in range(1,len(arr)):
        k = lcm(k,arr[i])
    return k
print(solution([2,6,8,14]))