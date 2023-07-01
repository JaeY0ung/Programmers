def solution(board):

    l = len(board)
    count = 0

    for x in range(l):
        for y in range(l):
            if board[x][y] == 1: # 지뢰가 있으면
                if x >= 1   and y >= 1   and  board[x-1][y-1] != 1: board[x-1][y-1] = 'X'
                if x >= 1   and               board[x-1][y] != 1:   board[x-1][y] = 'X'
                if x >= 1   and y <= l-2 and  board[x-1][y+1] != 1: board[x-1][y+1] = 'X'
                if y >= 1   and               board[x][y-1] != 1:   board[x][y-1] = 'X'
                if y <= l-2 and               board[x][y+1] != 1:   board[x][y+1] = 'X'
                if x <= l-2 and y >= 1   and  board[x+1][y-1] != 1: board[x+1][y-1] = 'X'
                if x <= l-2 and               board[x+1][y] != 1:   board[x+1][y] = 'X'
                if x <= l-2 and y <= l-2 and  board[x+1][y+1] != 1: board[x+1][y+1] = 'X'

    for x in range(l):
        for y in range(l):
            if board[x][y] == 0:
                count += 1
    
    return count
