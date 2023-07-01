from collections import deque as dq

def solution(people, limit):
    people = sorted(people, reverse = True)   #내림차순 정렬
    my_arr = dq(people)
    restnum = len(people)
    counting = 0
    while True:
        if restnum >=2:
            if my_arr[0] + my_arr[-1] > limit:
                my_arr.popleft()
                restnum -=1
            else:
                my_arr.popleft()
                my_arr.pop()
                restnum -= 2
                
            counting += 1
        elif restnum == 1:
            restnum -= 1
            my_arr.pop()
            counting += 1
        elif restnum == 0:
            break
    return counting

        
        


print(solution([70, 50, 80, 50], 100))
