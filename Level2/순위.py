from copy import deepcopy
def solution(n, results):
    answer = 0
    for i in range(1,n+1):
        x = deepcopy(results)
        left = []
        right = []
        count = 0
        while True:
            isTrue = True
            for vs in x:
                if vs[0] == i or vs[0] in right:
                    right.append(vs[1])
                    x.remove(vs)
                    count += 1
                    isTrue = False
                elif vs[1] == i or vs[1] in left:
                    left.append(vs[0])
                    x.remove(vs)
                    count += 1
                    isTrue = False
            if isTrue == True:
                break
        if count == n-1:
            answer += 1
    return answer