def solution(k,m,score):  #617위
    profit = 0
    score.sort(reverse = True)
    box = len(score) // m
    for i in range(0, box):
        profit += score[m*i + m - 1] * m
    return profit