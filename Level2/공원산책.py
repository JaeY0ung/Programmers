
#! 문제 설명
#? 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 
#? 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.
#? ["방향 거리", "방향 거리" … ]
#? 예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 
#? 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.
#? 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
#? 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
#? 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
#? 공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

from copy import deepcopy

def solution(park, routes):
    #? 행 열 길이 가져오기
    h = len(park)
    w = len(park[0])

    #? 방향 설정 
    directions = ['E','W','S','N']
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    #? 시작 지점 탐색
    for i in range(h):
        if 'S' in park[i]:
            j = park[i].index('S')
            now = [i,j]
            break

    #? 모든 명령 탐색
    for route in routes:
        direction, moves = route.split()[0], int(route.split()[1])
        index = directions.index(direction)
        
        
        is_possible = True   #? 이 명령을 따를 수 있는 지 없는 지 체크
        temp = deepcopy(now) #? 명령을 따를 수 있을 때만 now 동기화

        #? moves만큼 한칸 씩 이동하며 갈 수 있는 길인지 탐색
        for _ in range(moves):
            temp[0] += dx[index]
            temp[1] += dy[index]
            if temp[0] >= h or temp[0] < 0 or temp[1] >= w or\
            temp[1] < 0 or park[temp[0]][temp[1]] == 'X':
                is_possible = False
                break

        #? 가는 길이 공원을 벗어나지 않고 장애물이 없으면 간다.
        print(f'갈 수 있는길: {is_possible}')
        if is_possible == True:
            now = temp
        print(now)
    return now
