import copy
def solution(dirs):
    x1 = 0
    y1 = 0
    set1 = set()
    for i in dirs:
        x2 = x1
        y2 = y1
        if i == "U":
            if y1 != 5:
                y1 += 1
                set1.add((x1,y1,x2,y2))
    
        if i == "D":
            if y1 != -5:
                y1 -= 1
                set1.add((x2,y2,x1,y1))
        if i == "L":
            if x1 != -5:
                x1 -= 1
                set1.add((x2,y2,x1,y1))
        if i == "R":
            if x1 != 5:
                x1 += 1
                set1.add((x1,y1,x2,y2))
    return len(set1)

print(solution("ULURRDLLU"))
        
        