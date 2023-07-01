def solution(skill, skill_trees):
    skill_order_list = [_ for _ in skill]
    answer = 0
    for tree in skill_trees:
        str1 = ''
        for sk in tree:
            if sk in skill_order_list:
                str1 += sk
        print(str1)
        arr1 = []
        for i in str1:
            arr1.append(skill.index(i))
        print(arr1)

        if arr1 == [i for i in range(arr1[-1]+1)]:
            answer += 1
              
    return answer



print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))