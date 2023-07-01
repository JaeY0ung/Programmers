# 00 01     00 01 02   i0*m0+i1*m0  i0*01+i1*11  i0*02+i1*12
# 11 12  x  10 11 12 = 1*00+12*10  11*01+12*11  11*02+12*12
# 21 22
# n * m  m * k    n * k


def solution(arr1, arr2):
    n = len(arr1)    # arr1 행의 길이
    m = len(arr1[0]) # arr1 열의 길이
    k = len(arr2[0]) # arr2 열의 길이
    answer = [[] for _ in range(n)]
    for i in range(n):  # 0

        for j in range(k): # 0


            sum = 0
            for t in range(m):
                sum += arr1[i][t] * arr2[t][j]  #[0][]  [][]
            answer[i].append(sum)
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]] ))