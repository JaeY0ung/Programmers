def solution(gems):
    # gems: ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    l = len(gems)    # l: 8
    n = len(set(gems))
    gems_list = list(set(gems))
    print(gems_list)
    for j in range(n, l + 1):  # j: 4,5,6,7,8
        for i in range(l-j+1): # j:4 -> i: 0,1,2,3,4
            arr = gems[i:i+j]
            result = True
            for k in range(n):
                if arr.count(gems_list[k]) == 0:
                    result = False
                    break
            if result == True:
                return [i+1,i+j]

            # if arr.count("DIA") >= 1 and arr.count("RUBY") >= 1 and arr.count("EMERALD") >= 1 and arr.count("SAPPHIRE") >= 1:
            #     return [i+1,i+j]




def solution(gems):   #2
    # gems: ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    l = len(gems)    # l: 8
    n = len(set(gems))
    for j in range(n, l + 1):  # j: 4,5,6,7,8
        for i in range(l-j+1): # j:4 -> i: 0,1,2,3,4
            arr = gems[i:i+j]
            if len(set(arr)) == n:
                return [i+1,i+j]