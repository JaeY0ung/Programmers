def solution(arr1, arr2):
    row = len(arr1)
    column = len(arr1[0])
    answer = []
    for k in range(row):
        answer.append([])
        for _ in range(column):
            answer[k].append(0)
            
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
print(solution( [[1,2],[2,3]], [[3,4],[5,6]] ) )