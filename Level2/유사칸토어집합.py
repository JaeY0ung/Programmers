def solution(n, l, r):
    x = "1"
    for i in range(n):
        temp = ""
        l1 = len(x)
        for j in range(l1):
            if x[j] == "1":
                temp += "11011"
            else:
                temp += "00000"
        x = temp
    return x[l-1:r].count("1")