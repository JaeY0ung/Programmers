def solution(priorities, location):
    count = 0  # 인쇄된 순서.
    while True:
        l = len(priorities)
        result = True
        for j in range(1, l):
            if priorities[0]  < priorities[j]:  # 순위 낮으면 밀려남 
                priorities.append(priorities[0])
                del priorities[0]
                result = False
                if location == 0:
                    location = len(priorities)-1
                else:
                    location -= 1
                break
                
        if result == True: # 순위 높으면 사라지고, 순서up, 위치down
            del priorities[0]
            count += 1
            if location == 0:
                location = len(priorities)-1
                break
            else:
                location -= 1
    return count


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))