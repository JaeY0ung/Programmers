from math import sqrt

def gcd(a,b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

def solution(arrayA, arrayB):

    x = arrayA[0]
    for i in range(len(arrayA)):
        x = gcd(x, arrayA[i])
    while True:
        result = True
        if x == 1:
            ans = 0
            break
        for num in arrayB:
            if num % x == 0:
                result = False
                break
        if result == True:
            ans = x
            break
        else:
            for i in range(x-1,0,-1):
                if x % i == 0:
                    x = i
                    break
    ans1 = ans

    x = arrayB[0]
    for i in range(len(arrayB)):
        x = gcd(x, arrayB[i])
    while True:
        result = True
        if x == 1:
            ans = 0
            break
        for num in arrayA:
            if num % x == 0:
                result = False
                break
        if result == True:
            ans = x
            break
        else:
            for i in range(x-1,0,-1):
                if x % i == 0:
                    x = i
                    break
    ans2 = ans
    
    return max(ans1,ans2)

print(solution([10, 17], [5, 20]))
# print(solution([10, 20], [5, 17]))
    

    
    