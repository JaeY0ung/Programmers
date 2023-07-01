def solution(n, k):
    arr = []
    while True:
        arr.append(str(n % k))
        if n // k == 0:
            break
        n = n // k
        
    num = ''.join(arr[::-1])
    print(num)
    arr2 = num.split('0')
    def isSosu(x):
        if x == 1:
            return False
        if x == 2 or x == 3:
            return True
        else:
            isTrue = True
            for i in range(2,int(x**0.5)+1):
                if x % i == 0:   #소수가 아님
                    isTrue = False
                    break
            return isTrue
    result = 0
    print(arr2)
    for s in arr2:
        if s != '' and isSosu(int(s)) == True:
            result += 1
    return result
    
print(solution(437674, 3))
print(solution(110011, 10))