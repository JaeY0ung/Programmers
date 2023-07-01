def solution(s):
    str1 = ''
    l = len(s)
    
    if l % 2 == 0: #짝수
        str1 += s[(l//2)-1]
    str1 += s[l//2]

    return str1
        
#테스트 출력
print(solution("abcde"))
print(solution("qwer"))