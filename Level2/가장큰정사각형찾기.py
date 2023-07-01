

def solution(board):    # 테스트는 모두통과, 효율성 테스트는 모두 탈락.
    a = len(board)
    b = len(board[0])
    
    min_l = min(a, b)

    while True:
        for i in range(a - min_l + 1):
            for j in range(b - min_l + 1):
                for k in range(min_l):
                    if board[i+k][j: j + min_l] != [1 for _ in range(min_l)]:
                        break
                    if k == min_l - 1:
                        return min_l ** 2
        min_l -= 1
        if min_l == 0:
            return 0
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
