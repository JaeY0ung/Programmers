# from itertools import combinations as cb   #시간초과.
# def solution(orders, course):
#     yori_set = set()
#     result2 = []
#     for yori in orders:
#         for i in list(yori):
#             yori_set.add(i)
#     yori_list = sorted(list(yori_set))
#     # print(yori_list)
#     # print (list(cb(yori_list, 1)))
#     for i in course:  # 2
#         result = dict()
#         for j in list(cb(yori_list, i)): # A
#             count = 0
#             for k in orders:
#                 isTrue = True
#                 for x in j:
#                     if x not in k:
#                         isTrue = False
#                         break
#                 if isTrue == True:
#                     count += 1
#                 if k == orders[-1] and count >= 2:
#                     result["".join(j)] = count
#         # print(result)
#         # print(list(result.values()))
#         for i in list(result.keys()):
#             if result[i] == max(result.values()):
#                 result2.append(i)
                
#     return sorted(result2)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# # print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# # print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))



from itertools import combinations as cb
def solution(orders, course):
    result2 = []
    for k in course:
        answer = set()
        for i in orders:
            if len(i) >= k:
                answer.update( set( cb(list(i),k) ) )
        answer = list(answer)
        # print(answer)
        result = dict()
        for j in answer: # A
            count = 0
            for k in orders:
                isTrue = True  #모두 안에 있으면 count += 1
                for x in j:    
                    if x not in k:
                        isTrue = False
                        break
                if isTrue == True:
                    count += 1
                if k == orders[-1] and count >= 2:
                    result["".join(j)] = count

        for i in list(result.keys()):
            k = max(result.values())
            if result[i] == k:
                result2.append(i)
    return sorted(result2)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
