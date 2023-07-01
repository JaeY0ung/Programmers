def solution(a, b):  #5월 b일이면
    list = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    # 1월 1일부터 떨어진 날
    for i in range(a-1):  # i = 0,1,2,3 (1,2,3,4월)
        sum += list[i]
    sum += b-1
    if sum % 7 == 0:
        return "FRI"
    elif sum % 7 == 1:
        return "SAT"
    elif sum % 7 == 2:
        return "SUN"
    elif sum % 7 == 3:
        return "MON"
    elif sum % 7 == 4:
        return "TUE"
    elif sum % 7 == 5:
        return "WED"
    else:
        return "THU"
