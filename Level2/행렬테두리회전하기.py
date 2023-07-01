def solution(rows, columns, queries):
    # arr1 = [[rows * i + j + 1 for j in range(columns)] for i in range(rows)]  # 초기설정.  -> 여기서 맨앞 \
    # rows를 columns 로 잘못 적었음.
    arr1 = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]  # 초기설정.
    answer = []
    for x in queries:

        x1, y1, x2, y2 = x[0] - 1 , x[1]- 1 , x[2]- 1 , x[3] - 1
        minNum = arr1[x1][y1]
        temporaryNum = arr1[x1][y1]
        for k in range(x1,x2):
            arr1[k][y1] = arr1[k+1][y1]
            minNum = min(arr1[k][y1], minNum)
        for k in range(y1,y2):
            arr1[x2][k] = arr1[x2][k+1]
            minNum = min(arr1[x2][k], minNum)
        for k in range(x1, x2):
            arr1[x1+x2-k][y2] = arr1[x1+x2-k-1][y2]
            minNum = min(arr1[x1+x2-k][y2], minNum)
        for k in range(y1,y2-1):
            arr1[x1][y1+y2-k] = arr1[x1][y1+y2-k-1]
            minNum = min(arr1[x1][y1+y2-k], minNum)
        arr1[x1][y1+1] = temporaryNum
        # print(arr1)
        minNum = min(arr1[x1][y1+1], minNum)
        answer.append(minNum)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#print(solution(100, 97, [[1,1,100,97]]))