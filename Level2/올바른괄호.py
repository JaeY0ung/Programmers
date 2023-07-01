def solution(s):   # 테스트는 통과, 효율성은 X
    while "()" in s:
        x = s.index("()")
        s = s[0:x] + s[x+2:]
    if s == '':
        return True
    else:
        return False


def solution(s):
    s1 = ''
    for x in s:
        s1 += x
        if '()' in s1:
            del s1[-2:]
    if s == '':
        return True
    else:
        return False



def solution(s):
    s1 = []
    for x in s:
        if s1 == []:
            s1.append(x)
        else:
            if x == ')':
                if s1[-1] == '(':
                    del s1[-1]
                else:
                    s1.append(x)
            else:
                s1.append(x)
    print(s1)
    if s1 == []:
        return True
    else:
        return False
        
        





