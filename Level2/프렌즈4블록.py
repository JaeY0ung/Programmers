def solution(m, n, board):
    answer = 0
    colist = []
    while True:
        isTrue = True
        for i in range(m-1): # 행
            for j in range(n-1): # 열
                if board[i][j] != '0' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    isTrue = False
                    colist.append((i,j))
                    colist.append((i,j+1))
                    colist.append((i+1,j))
                    colist.append((i+1,j+1))
        colist = list(set(colist))
        print(colist)
        answer += len(colist)
        print(colist)
        for x in list(colist):
            board[x[0]][x[1]] == '0'
        print(board)
        
        
        if isTrue == True:
            break
            
        

# print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))