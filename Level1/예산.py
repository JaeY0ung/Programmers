def solution(d, budget):
    d1 = sorted(d)
    count = 0
    sum = 0
    for i in d1:
        count += 1
        sum += i
        if sum > budget:
            return count - 1
            break
    if count == len(d):
        return count