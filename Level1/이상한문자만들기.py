# from math import ceil, floor

# def solution(s):
#     for i in range(ceil(len(s)/2)) :
#         s[2*i].upper()
#     for i in range(floor(len(s)/2)) :    
#         s[2*i+1].lower()
#     return s

def solution(s):
    p = ""
    j = 1
    for i in range(len(s)):
        if s[i] == ' ':
            j = i   # j에 공백이 몇번째인지 저장.
            
        if (i-j + 1) % 2 == 0 :
            p += s[i].upper()
        else:
            p += s[i].lower()
    return p


print(solution("try hello world"))
