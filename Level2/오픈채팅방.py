def solution(record):

    user_set = set()

    for rec in record:
        x = rec.split()[1]
        user_set.add(x)   # ['Enter', 'uid1234', 'Muzi']

    user_list = list(user_set)         # ['uid1234', 'uid4567']
    nickname_list = [ "" for _ in user_list] # ['', '']

    for rec2 in record:                # nickname_list = ['Ryan', 'Prodo']
        if rec2.split()[0] != "Leave":
            i = user_list.index(rec2.split()[1])
            nickname_list[i] = rec2.split()[2]  

    answer = []
    
    for rec3 in record:
        i = user_list.index(rec3.split()[1])
        if rec3.split()[0] == "Enter":
            answer.append("%s님이 들어왔습니다."% nickname_list[i])
        elif rec3.split()[0] == "Leave":
            answer.append("%s님이 나갔습니다."% nickname_list[i])

    return answer
    # user_list = []
    # nickname_list = []
    # for rec2 in record:
    #     if rec2.split()[0] == "Enter":
    #         user_list.append(rec2.split()[1])
    #         nickname_list.append(rec2.split()[2])
    #     elif rec2.split()[0] == "Leave":
    #         i = user_list.index(rec2.split()[1])
    #         nickname_list[i] = 
    # print(nickname_list)




print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
