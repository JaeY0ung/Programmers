def solution(n, t, m, p):
    arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    list1 = []   # 게임 숫자 배열 리스트
    for i in range(t*m):
        list2 = []
        while True:
            list2.append(arr[i % n])
            i = i // n
            if i == 0:
                break
        list1.extend(list2[::-1])
        if len(list1) >= t * m:
            break
    result = ''.join([list1[p-1+m*k] for k in range(t)])
    return result

print(solution(2,4,2,1))
print(solution(16,16,2,2))
    

