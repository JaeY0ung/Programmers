
def solution(board):   

    a = len(board) #행의 길이
    b = len(board[0]) #열의 길이
    l = min(a,b)  #정사각형 최대 크기
    n = l #정사각형 변의 길이.

    # while True:     #효율성 테스트만 통과 못함 ㅠㅠ
    #     for x in range(a-n+1):
    #         for y in range(b-n+1):
    #             isone = True
    #             for s in range(x, x+n):
    #                 for t in range(y, y+n):
    #                     if board[s][t] == 0:
    #                         isone = False
    #                         break
    #                 if isone == False:
    #                     break
    #             if isone == True:
    #                 return n ** 2
    #     n -= 1

    while True:   #8 런타임 에러
        for x in range(a-n+1):
            for y in range(b-n+1):
                my_arr = [board[s][y: y+n] for s in range(x, x+n)]
                if min(my_arr) == [1 for _ in range(n)]:
                    return n ** 2
        n -= 1
                    

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))