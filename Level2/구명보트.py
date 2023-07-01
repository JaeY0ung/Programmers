def solution(people, limit):   #시간초과.
    people = sorted(people,reverse = True)
    answer = 0
    while True:
        if len(people) <= 1:
            break
        for i in range(1, len(people)):
            if people[0] + people[i] <= limit:
                del people[i]
                del people[0]
                answer += 1
                break
            if i == len(people) - 1:
                del people[0]
                answer += 1
    if len(people) == 1:
        answer += 1
        
    return answer

print(solution([70,50,80,50], 100))

