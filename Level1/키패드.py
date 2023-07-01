def solution(numbers, hand):
    answer = ''
    L_location = (3,0)
    R_location = (3,2)
    
    for i in numbers: 
        if i == 1 or i == 4 or i ==7:
            answer += 'L'
            L_location = (i // 3, 0)    # 0,0 시작
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            R_location = (i // 3 - 1, 2)
        else: # i % 3 == 2:
            if i != 0:
                i_location = (i // 3, 1)
            else:
                i_location = (3, 1)
                
            (a1,b1) = L_location
            (a2,b2) = R_location
            (a3,b3) = i_location
            L_distance = abs(a1-a3) + abs(b1-b3)
            R_distance = abs(a2-a3) + abs(b2-b3)
            if L_distance < R_distance:
                answer += 'L'
                L_location = i_location
            elif L_distance > R_distance:
                answer += 'R'
                R_location = i_location
            elif L_distance == R_distance:
                if hand == 'left':
                    answer += 'L'
                    L_location = i_location
                elif hand == 'right':
                    answer += 'R'
                    R_location = i_location    
    return answer