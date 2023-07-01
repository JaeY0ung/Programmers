# def solution(X, Y):
#     listX = []
#     listY = []
#     maxList = []

#     str1 = ''
#     for i in range(10):
#         listX.append(X.count(str(i)))
#         listY.append(Y.count(str(i)))
    
#     for j in range(10):
#         maxList.append(min(listX[j], listY[j]))
    
#     for k in range(10):
#         str1 += str((9-k)) * maxList[9 - k]
#     if maxList == [0 for _ in range(10)]:
#         return "-1"
#     else:
#         return str(int(str1))



# def solution(X, Y):
#     str1 = ''
#     i = 9
#     while i >= 0 :
#         str1 += str(i) * min(X.count(str(i)), Y.count(str(i)))
#         i -= 1

#     if str1 == '':
#         return "-1"
#     else:
#         return str(int(str1))

# print(solution("100","2345"))
# print(solution("100","203045"))


# def solution(X, Y):
#     lx = len(X)
#     ly = len(Y)
#     listX = [0 for _ in range(10)]
#     listY = [0 for _ in range(10)]
#     s1 = ''
#     for i in range(lx):
#         listX[int(X[i])] += 1
#     for k in range(ly):
#         listY[int(Y[k])] += 1

#     j = 9
#     while j >= 0:
#         s1 += str(j) * min(listX[j], listY[j])
#         j -= 1

#     if s1 == '':
#         return "-1"
#     else:
#         return str(int(s1))

def solution(X, Y):
    arrX = sorted(X)
    arrY = sorted(Y)
    lx = len(X)
    ly = len(Y)
    listX = [0 for _ in range(10)]
    listY = [0 for _ in range(10)]
    s1 = ''
    j = 0
    for i in range(lx-1):
        if arrX[i] != arrX[i+1]:
            listX[int(arrX[i])] = i - j + 1
            j = i + 1
        listX[int(arrX[-1])] = lx - j
    j = 0
    for i in range(ly-1):
        if arrY[i] != arrY[i+1]:
            listY[int(arrY[i])] = i - j + 1
            j = i + 1
        listY[int(arrY[-1])] = ly - j

    j = 9
    while j >= 0:
        s1 += str(j) * min(listX[j], listY[j])
        j -= 1

    if s1 == '':
        return "-1"
    else:
        return str(int(s1))

print(solution("100","2345"))
print(solution("100","203045"))
