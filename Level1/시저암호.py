from curses.ascii import isdigit


def solution(s, n):
    small = 'abcdefghijklmnopqrstuvwxyz'   # 26개
    big = small.upper()
    str1 = ""
    
    for i in range(len(s)):
        if s[i] == " ":
            str1 += " "
        else:
            if s[i].isupper() == True: # 대문자
                str1 += big[(big.index(s[i]) + n + 1) % 26 - 1]
            else:  # 소문자
                str1 += small[(small.index(s[i]) + n + 1)% 26 - 1]
        
    return str1

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
