def solution(str1, str2):
    # 1. 소문자화
    str1 = str1.lower()
    str2 = str2.lower()
    # 2. 다중집합 정의
    arr1 = []
    arr2 = []
    # 3. 다중집합에 원소 추가
    for i in range(0, len(str1)-1):
        x = str1[i:i+2]
        if x.isalpha() == True:
            arr1.append(x)
    for i in range(0, len(str2)-1):  # 원소 추가
        x = str2[i:i+2]
        if x.isalpha() == True:
            arr2.append(x)
    # 합집합
    arr1_temp = arr1.copy()
    arr1_result = arr1.copy()
    for s1 in arr2:
        if s1 not in arr1_temp:
            arr1_result.append(s1)
        else:
            arr1_temp.remove(s1)
    # 교집합
    result = []
    for i in arr2:
        if i in arr1:
            arr1.remove(i)
            result.append(i)
            
    if len(arr1_result) == 0:
        return 65536
    else:
        return int(len(result)/len(arr1_result)*65536)