def solution(numlist, n):   # 테스트4 만 실패
    if len(numlist) == 1:
        return numlist
    numlist.sort(reverse = True)
    distance_dict = dict()
    for num in numlist:
        distance_dict[num] = abs(num-n)
    return list(dict(sorted(distance_dict.items(), key = lambda x: x[1])))
    