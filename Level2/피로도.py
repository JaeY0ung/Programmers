from itertools import permutations as p

def solution(k, dungeons):
    myarr = [i for i in range(len(dungeons))]
    perOfMyarr = list(p(myarr, len(myarr)))
    resultSet = set()
    # print(perOfMyarr)
    for piroarr in perOfMyarr:
        count = 0
        myP = k
        for num in piroarr:
            if dungeons[num][0] > myP:
                resultSet.add(count)
                break
            elif dungeons[num][0] <= myP:
                myP -= dungeons[num][1]
                count += 1
            if count == len(dungeons):
                return count
            print(myP)
        print("ㅡㅡㅡㅡㅡㅡㅡㅡ")
    return max(list(resultSet))
            


print(solution(80, [[80,20],[50,40],[30,10]]))