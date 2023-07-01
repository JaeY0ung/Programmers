def solution(a, b):
    num = yaksu(a,b)
    while True:
        if num % 5 == 0:
            num = num // 5
        elif num % 2 == 0:
            num = num // 2
        else:
            if num == 1:
                return 1
            else:
                return 2
    
def yaksu(a, b):
    mini = min(a,b)
    isTrue = True
    if b == 1 or b == 2:
        return 1
    if a == 1:
        pass
    elif a == 2:
        pass
    for i in range(2, mini + 1):
        if a % i == 0 and b % i == 0:
            a = a//i
            b = b//i
            isTrue = False
            return yaksu(a, b)
    if isTrue == True:
        return b