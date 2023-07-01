def solution(s):    # "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    #print(s)       #  ['2', '2,1', '2,1,3', '2,1,3,4']
    answer = []
    for i in s:
        ii = i.split(',') # ii = '2'    '2', '1'      '2', '1', '3'
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
    


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))