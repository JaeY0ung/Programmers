def solution(places):
    result = []
    for i in range(5):
        for j in range(5):
            sum = ""
            for k in range(5):
                sum += places[i][k][j]
            places[i].append(sum)
    print(places)
    for arr in places:
        isTrue1 = True
        for i in arr:
            if ("PP" in i) or ("POP" in i):  # 거리두기 안지킴.
                result.append(0)
                isTrue1 = False
                break
        if isTrue1 == True:   # 거리두기 지킴.
            result.append(1)
    return result
                
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))