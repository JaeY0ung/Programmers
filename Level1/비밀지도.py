def solution(n, arr1, arr2):
    arr3 = []
    arr4 = []
    for i in range(n): 
        arr3.append( bin( arr1[i] | arr2[i] + 2 ** n ) )
        str1 = ""  
        for j in range(n):
            if arr3[i][j-n] == "1" :
                str1 += "#"
            else:
                str1 += " "
        arr4.append(str1)
    
    return arr4

print( solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28] ) )
    