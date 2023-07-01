def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    arr = []
    for i in lost: # 중복제거.
        if i in reserve:
            arr.append(i)
    for k in arr:
        lost.remove(k)
        reserve.remove(k)
    for j in reserve:
        if j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
    return n - len(lost)

print(solution(5, [2,4], [1,3,5]))
print(solution(3, [3], [1]))
