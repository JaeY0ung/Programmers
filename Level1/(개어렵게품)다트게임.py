def solution(dartResult): # "1S2D*3T"
    l = len(dartResult)   # 7
    arr1 = []
    for i in range(l):
        if dartResult[i] in [str(j) for j in range(10)]: # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   i = 0 2 5
            if dartResult[i+1] != "0":
                if dartResult[i+1] == "S":
                    arr1.append(int(dartResult[i]))
                elif dartResult[i+1] == "D":
                    arr1.append(int(dartResult[i]) ** 2)
                elif dartResult[i+1] == "T":
                    arr1.append(int(dartResult[i]) ** 3)
                if i <= l - 3:
                    if dartResult[i+2] == "*":
                        if len(arr1) == 3 or len(arr1)==2 :
                            arr1[-2] += arr1[-2]
                            arr1[-1] += arr1[-1]
                        else: #len(arr1) == 1
                            arr1[0] += arr1[0]
                    if dartResult[i+2] == "#":
                        arr1[-1] = -arr1[-1]
            else: # i+1: 0일때
                if dartResult[i+2] == "S":
                    arr1.append(int(dartResult[i:i+2]))
                elif dartResult[i+2] == "D":
                    arr1.append(int(dartResult[i:i+2]) ** 2)
                elif dartResult[i+2] == "T":
                    arr1.append(int(dartResult[i:i+2]) ** 3)
                if i <= l - 4:
                    if dartResult[i+3] == "*":
                        if len(arr1) == 3 or len(arr1)==2 :
                            arr1[-2] += arr1[-2]
                            arr1[-1] += arr1[-1]
                        else: #len(arr1) == 1
                            arr1[0] += arr1[0]
                    if dartResult[i+2] == "#":
                        arr1[-1] = -arr1[-1]
    print(arr1)
    return sum(arr1)

print(solution("1S2D*3T"))
print(solution(	"1D2S#10S"))
