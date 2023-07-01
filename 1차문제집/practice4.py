# def solution(beginning, target):
#     n = len(beginning)
#     count = 0
#     def columnchange(x):  # x행 바꾸기.
#         for y in range(n):
#             beginning[x][y] = 1 - beginning[x][y]
#     def rowchange(y):  # y열 바꾸기.
#         for x in range(n):
#             beginning[x][y] = 1 - beginning[x][y]

#     for i in range(n):
#         if beginning[i][0] != target[i][0]:
#             columnchange(i)
#             count += 1
#     for j in range(1, n):
#         if beginning[0][j] != target[0][j]:
#             rowchange(j)
#             count += 1

#     if beginning == target:
#         return count
#     else:
#         return -1

# def solution(beginning, target):

#     n = len(beginning)
#     count1 = 0
#     count2 = 0
#     beginning1 = beginning
#     beginning2 = beginning

#     def columnchange(x, r):  # x행 바꾸기.
#         for y in range(n):
#             r[x][y] = 1 - r[x][y]
#     def rowchange(y, r):  # y열 바꾸기.
#         for x in range(n):
#             r[x][y] = 1 - r[x][y]

#     for i in range(n):
#         if beginning1[i][0] != target[i][0]:
#             columnchange(i, beginning1)
#             count1 += 1
#     for j in range(1, n):
#         if beginning1[0][j] != target[0][j]:
#             rowchange(j, beginning1)
#             count1 += 1
    
#     for _ in range(n):
#         if beginning2[0][_] != target[0][_]:
#             rowchange(_, beginning2)
#             count2 += 1

#     for __ in range(1, n):
#         if beginning2[__][0] != target[__][0]:
#             columnchange(__, beginning2)
#             count2 += 1 

#     print(f'{beginning1}\n{beginning2}')

#     if beginning1 != target:
#         count1 = 50
#     if beginning2 != target:
#         count2 = 50
#     print(count1, count2)

#     if count1 == 50 and count2 == 50:
#         return -1
#     else:
#         return min(count1, count2)

def solution(beginning, target):
    n = len(beginning)
    beginning1 = beginning
    count = 0
    def columnchange(x):  # x행 바꾸기.
        for y in range(n):
            beginning1[x][y] = 1 - beginning1[x][y]
    def rowchange(y):  # y열 바꾸기.
        for x in range(n):
            beginning1[x][y] = 1 - beginning1[x][y]

    for i in range(n):
        if beginning1[i][0] != target[i][0]:
            columnchange(i)
            count += 1
    for j in range(1, n):
        if beginning1[0][j] != target[0][j]:
            rowchange(j)
            count += 1
    count1 = count

    beginning1 = beginning
    count = 0
    for j in range(n):
        if beginning1[0][j] != target[0][j]:
            rowchange(j)
            count += 1
    for i in range(1, n):
        if beginning1[i][0] != target[i][0]:
            columnchange(i)
            count += 1
    count2 = count

    
    min(count1, count2)

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))