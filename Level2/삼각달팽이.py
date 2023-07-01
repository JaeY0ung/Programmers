def solution(n):
    answer = [[0 for _ in range(i+1)] for i in range(n)]
    x = 0
    y = 0
    num = 1
    answer[0][0] = 1
    isTrue = True
    
    while True:
        while True :
            if x <= n-2 and answer[x+1][y] == 0:
                if num == n*(n+1) // 2:
                    isTrue = False
                    break
                x += 1
                answer[x][y] = num
                num += 1
                    
        while True:
            if x <= n-2 and answer[x][y+1] == 0:
                if num == n*(n+1) // 2:
                    isTrue = False
                    break
                y += 1
                answer[x][y] = num
                num += 1
                
        while True:
            if x >= 1 and answer[x-1][y-1] == 0:
                if num == n*(n+1) // 2:
                    isTrue = False
                    break
                x -= 1
                y -= 1
                answer[x][y] = num
                num += 1
        if isTrue == False:
            break

    print(answer)

print(solution(4))