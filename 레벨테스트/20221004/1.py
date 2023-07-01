from math import ceil

def solution(n, stations, w):
    gizi=[]
    for i in stations:
        gizi.extend(list(range(i-w, i+w+1)))

    answer = 0

    j = 0
    for i in range(1, n+1):
        if i not in gizi:
            if 
            if i - 1 != j:
                j = i
            else:

            

    return answer
    


print(solution(11,[4,11],1))