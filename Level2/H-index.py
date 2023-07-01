def solution(citations):

    my_max = max(citations)  # 리스트 내 최대값
    l = len(citations)      # 리스트 길이
    h = my_max  

    while True:
        count_citations = 0   # 인용논문횟수

        for i in range(l):
            if citations[i] >= h:
                count_citations += 1
        
        if count_citations >= h:
            return h
        else:
            h -= 1
            
print(solution([3, 0, 6, 1, 5]))