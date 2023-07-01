def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    dict1 = dict()
    dict2 = dict()

    for i in range(len(str1)-1):
        if str1[i:i+2].isalnum() == True:
            a.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j:j+2].isalnum() == True:
            b.append(str2[j:j+2])

    for x in list(set(a)):    # {'an': 1, 'ke': 1, 'sh': 1, 'ha': 2, 'ak': 1, 'nd': 1, 'ds': 1}
        dict1[x] = a.count(x)
    for y in list(set(b)):    # {'an': 1, 'ke': 1, 'sh': 1, 'ak': 1, 'ha': 2, 'nd': 1, 'ds': 1}
        dict2[y] = b.count(y)

    myarr = []
    myarr.extend(list(dict1.keys()))
    myarr.extend(list(dict2.keys()))
    myarr = list(set(myarr))

    maxnum = 0
    minnum = 0

    for x in myarr:
        try:
            k = dict1[x]
        except:
            k = 0
        try:
            s = dict2[x]
        except:
            s = 0
        maxnum += max(k,s)
        minnum += min(k,s)
    return minnum/maxnum * 65536

print(solution('handshake', 'shake hands'))