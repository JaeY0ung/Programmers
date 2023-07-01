
def solution(s):
    length_s = len(s)
    small = ''
    big = ''
    for i in range(length_s):
        if s[i].isupper() == True:
            big += s[i]
        else:
            small += s[i]
    small = ''.join(sorted(small, reverse = True))
    
    big = ''.join(sorted(big, reverse = True))
    return small + big

print(solution("Zbcdefg"))