def solution(ingredient):   # 601위
    myarr = []
    for thing in ingredient:
        myarr.append(thing)
        if len(myarr) >= 4 and myarr[-4:] == [1,2,3,1]:
            del myarr[-4:]
            count += 1
    return count