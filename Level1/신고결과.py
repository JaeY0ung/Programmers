def solution(id_list, report, k):
    #1.  중복 없애기.
    id_singo_num_list = [0 for _ in id_list]
    id_singo_list = []
    report = list(set(report))
    result = [0 for __ in id_list]

    for singo in report:  # 신고당한횟수 리스트
        id_singo_num_list[ id_list.index(singo.split()[-1]) ] += 1
    # print(id_singo_num_list)  # [1, 2, 0, 2]

    for i in range(len(id_singo_num_list)):
        if id_singo_num_list[i] >= k:
            id_singo_list.append(id_list[i])
    # print(id_singo_list)  # ['frodo', 'neo']  k번 이상 신고당한 사람.

    for k in report:
        if k.split()[-1] in id_singo_list:
            result[id_list.index(k.split()[0])] += 1
    return result



print(solution(["muzi", "frodo", "apeach", "neo"], \
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))