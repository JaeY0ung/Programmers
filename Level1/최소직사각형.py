def solution(sizes):
    num = len(sizes)
    for j in range(num):
        if sizes[j][0] > sizes[j][1]:  # 모두 가로< 세로로 만들기.
            sizes[j][0], sizes[j][1] = sizes[j][1], sizes[j][0]
    list1 = [sizes[i][0] for i in range(num)]
    list2 = [sizes[i][1] for i in range(num)]
    answer = max(list1) * max(list2)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))