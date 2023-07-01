from itertools import product as pro

def solution(triangle):
    height = len(triangle)
    myarr = list(pro([0,1],repeat = height))
    resultSet = set()
    # print(myarr)
    for arr in myarr:
        x = 0
        sum = 0
        for i in range(height):
            sum += triangle[i][x]
            x += arr[i]
        resultSet.add(sum)
    return max(list(resultSet))

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
