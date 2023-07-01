def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    answer = sum
    return answer

print(solution([4,7,12], [True, False, True]))