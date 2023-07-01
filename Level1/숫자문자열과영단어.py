def solution(s):
    list = [[0,'zero'], [1,"one"], [2, 'two'], \
        [3, 'three'],[4,'four'],[5,'five'], [6,'six'], \
            [7,'seven'], [8,'eight'],[9,'nine']]
    for i in range(len(list)):
            s = s.replace(list[i][1], str(list[i][0]))
    answer = int(s)
    return answer
s = "one4seveneight"
print(solution(s))