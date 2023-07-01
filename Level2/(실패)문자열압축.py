from math import ceil
def solution(s):   # "abcabcabcabcdededededede"  24글자
    l = len(s)
    for i in range(1, l + 1):   # 길이i 인 문자열들로 슬라이스
        arr1 = []
        for j in range(ceil(l/i) - 1):
            arr1.append(s[i*j: i*(j +1)])
        arr1.append(s[i*(ceil(l/i)-1):])

        print(arr1)
        
        str_arr1 = ''
        for elements in arr1:
            str_arr1 += str(arr1.count(elements)) + ''
            for _ in range(arr1.count(elements)):
                arr1.remove(elements)





print(solution("abcabcabcabcdededededede"))
