
def solution(n, times):
    a = 1
    b = min(times) * n
    while True:
        sum = 0
        for t in times:
            sum += ((a+b)//2) // t
        if sum == n:
            print(a,b)
            break
        elif sum > n:
            a = (a + b) // 2
        else:
            b = (a + b) // 2
        print(a,b)

        

        
print(solution(6, [7, 10]))

