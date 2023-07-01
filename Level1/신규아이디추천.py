def solution(new_id):
    id1 = new_id.lower()   #1
    
    id2 = ''       #2
    for i in range(len(id1)): 
        if id1[i] in ["a","b","c","d","e","f",\
            "g","h","i","j","k","l","m","n","o","p",\
                "q","r","s","t","u","v","w","x","y",\
                    "z","_","-",".","0","1","2","3"\
                        ,"4","5","6","7","8","9"]:
            id2 += id1[i]
    print(id2)

    while ".." in id2:   #3
        id2 = id2.replace('..', '.')
    id3 = id2
    print(id3)
    if len(id3) > 0:
        if id3[0] == ".":  #4
            id3 = id3[1:]
    if len(id3) > 0:
        if id3[-1] == ".":
            id3 = id3[:-1]
    id4 = id3
    print(id4)

    if id4 == '':   #5
        id4 += "a"
    id5 = id4
    print(id5)

    if len(id5) >= 16:  #6
        id5 = id5[:15]
        if id5[-1] == ".":
            id5 = id5[:14]
    id6 = id5
    print(id6)

    if len(id6) <= 2:
        while len(id6) < 3: #7
            id6 += id6[-1]
    id7 = id6
    
    return id7

print(solution("123_.def"))