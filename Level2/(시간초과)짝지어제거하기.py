
# 이게 내 풀이  시간초과.

def solution(s):    # 'baabaa'
    l = list(s)     # l ; list
    while True:
        count = 0
        i = 0
        while i < len(l) - 1:
            if l[i] == l[i+1]:   #1: bbaa
                del l[i: i+2]
                count += 1
            else:
                i += 1
        if count == 0:
            break


    if l == []:
        return 1
    else:
        return 0   # 1,2,9,10,11,12,13 통과 / 효율성테스트 모두 통과 X


print(solution('baabaa'))



def solution(s):    # 이게 답.
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0 
