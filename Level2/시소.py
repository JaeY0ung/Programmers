def solution(weights):
    
    rightratio = [1,1.5,2,1.33333]
    l = len(weights)
    count = 0
    weights.sort()
    for i in range(l-1):
        for j in range(i+1,l):
            mini = min(weights[i],weights[j])
            maxi = max(weights[i],weights[j])
            if round(maxi/mini,5) in rightratio:
                count += 1
                
    return count


def solution(weights):
    
    rightratio = [1,1.5,2,4/3]
    count = 0
    weights.sort()
    for i in range(len(weights)):
        for ratio in rightratio:
            count += weights[i+1:].count(weights[i] * ratio)
    return count


    for i in



    