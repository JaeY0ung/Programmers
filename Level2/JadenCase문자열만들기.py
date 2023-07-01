# JadenCase 문자열 만들기

# def solution(s):
#     gongbaekarr = []   # 공백이 몇번째 인덱스에 있는지 리스트.
#     for i in range(len(s)):
#         if s[i] == ' ':
#             gongbaekarr.append(i)
            
#     arr1 = s.split()   # 문자열 슬라이스.
#     numarr = [str(i) for i in range(10)]
#     answer = ''
#     while True:
#             if len(answer) in gongbaekarr:
#                 answer += ' '
#             else:
#                 break
#     for word in arr1:
#         if word[0] in numarr:
#             answer += word
#         else:
#             answer += word.capitalize()
#         while True:
#             if len(answer) in gongbaekarr:
#                 answer += ' '
#             else:
#                 break
                
#     return answer


from curses.ascii import isdigit

def solution(s):
    answer = ''
    count = 0
    for mystr in s:
        if mystr == ' ':
            answer += ' '
            count = 0
        elif isdigit(mystr) == True:
            count = 1
            answer += mystr
        elif count == 0:
            count = 1
            answer += mystr.upper()
        elif count == 1:
            answer += mystr.lower()
    return answer

        