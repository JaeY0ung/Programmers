def solution(name):
    alphabets = ["A","B","C","D","E","F","G","H","I","J",\
                "K","L","M","N","O","P","Q","R",\
                "S","T","U","V","W","X","Y","Z"]  #26
    l = len(name)
    sum1 = 0  # sum1 : 위아래 이동 횟수
    for s1 in name:
        if alphabets.index(s1) > 13:
            sum1 += 26 - alphabets.index(s1)
        else:
            sum1 += alphabets.index(s1)

    sum2 = l - 1   # sum2 : 좌우 이동 횟수
    num1 = 0
    num2 = 0
    if name[-1] == "A":
        for i in range(1, len(name)):
            if name[-i] == "A":
                num1 += 1
            else:
                break

    if name[1] == "A":
        for i in range(1, len(name)):
            if name[i] == "A":
                num2 += 1
            else:
                break
    for i in range(l+1):
        if "A" * (l-i) in name:
            s = 1 - i
            k = name.index("A" * (l-i))
            num3 = max( l - 1 - (l + k - s -2), l - 1 - (2 * l - k -2 * s -1) )
            break
        if i == l:
            num3 = 0
            
    num = max(num1, num2, num3)
    
    return sum1 + sum2 - num

print(solution("JEROEN"))