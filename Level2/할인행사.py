def solution(want, number, discount):  # 깔끔히 완료!  635위
    l = len(discount)
    ans = 0
    for i in range(l-9):

        result = True
        itemdict = dict()  # dict 생성
        for thing in discount[i: i+10]:
            if thing in itemdict:
                itemdict[thing] += 1
            else:
                itemdict[thing] = 1
        for s in range(len(want)):
            if want[s] not in itemdict.keys():
                result = False
                break
            elif itemdict[want[s]] < number[s]:
                result = False
                break
            
        if result == True:
            ans += 1
    
    return ans

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))