def solution(board, moves):
    list = []
    count = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                list.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
            else:
                continue
        for k in range(len(list) - 1):
            if list[k] == list[k+1]:
                del list[k:]
                count += 2
    answer = count
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))