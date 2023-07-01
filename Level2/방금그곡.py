def solution(m, musicinfos):
    splitData = []
    answerDic = dict()
    for data in musicinfos:
        splitData.extend("".join(data).split(","))


    for i in range(3, len(splitData), 4):
        akbo = splitData[i]  #악보
        l = len(akbo) # 악보길이
        time = int(splitData[i-2][-2:]) - int(splitData[i-3][-2:])   #시간
        repeatnum = time // l # 반복된 횟수.
        restnum = time % l  # 남은 횟수
        music = akbo * repeatnum
        music = music + akbo[:restnum]
        
        if m in music:
            answerDic[time] = splitData[i-1]  # 딕셔너리에 시간,제목 데이타 저장
    # print(answerDic)


    if len(answerDic) == 0:
        return None
    else:
        answerDic = dict(sorted(answerDic.items()))
        return list(answerDic.values())[0]


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))