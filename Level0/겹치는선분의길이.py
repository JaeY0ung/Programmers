def solution(lines):
    answer = set()
    sum1 = 0
    for i in range(2):
        for j in range(i+1,3):
            mini = max(lines[i][0], lines[j][0])
            maxi = min(lines[i][1], lines[j][1])
            if mini < maxi:
                for x in range(mini, maxi):
                    answer.add(tuple(list([x, x + 1])))
    for arr in answer:
        sum1 += arr[1]-arr[0]
    return sum1
print(solution([[0, 1], [2, 5], [3, 9]]))