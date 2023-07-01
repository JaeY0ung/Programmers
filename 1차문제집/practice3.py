def solution(order):
    containerBelt = [i+1 for i in range(len(order))] # [1,2,3,4,5]    #앞에서부터 빼고 넣음.
    bozoBelt = []    # 뒤에서부터 넣고 뺌.
    bozoBelt.extend(containerBelt[ :order[0] - 1])   # containerBelt[num-1] 은 트럭으로.
    containerBelt = containerBelt[order[0]: ]
    count = 1
    
    for things in order[1:]:

        # if things in containerBelt:
        #     x = containerBelt.index(things)
        #     bozoBelt.extend(containerBelt[ : x])
        #     containerBelt = containerBelt[ x + 1 : ]
        #     count += 1
            
        if bozoBelt ==[]:
            if things in containerBelt:
                x = containerBelt.index(things)
                bozoBelt.extend(containerBelt[ : x])
                containerBelt = containerBelt[ x + 1 : ]
                count += 1
            else:
                break
        
        elif bozoBelt !=[]:
            if bozoBelt[-1] == things:
                count += 1
                del bozoBelt[-1]
            elif things in containerBelt:
                x = containerBelt.index(things)
                bozoBelt.extend(containerBelt[ : x])
                containerBelt = containerBelt[ x + 1 : ]
                count += 1
            else:
                break

    return count
        
print(solution([4,3,1,2,5]))
print(solution([5,4,3,2,1]))