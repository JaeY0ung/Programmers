def solution(s):
    l = len(s)
    res = []
    for i in range(l):
        t = True
        for j in range(1, i+1): # j: 간격
            if s[i-j] == s[i]:
                res.append(j)
                t = False
                break
        if t == True:
            res.append(-1)
        print(res)
    return res

print(solution("banana"))