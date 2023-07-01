def solution(s):
    trans_count = 0
    zero_count = 0
    while s != "1":
        zero_count += s.count('0')
        s = bin(s.count('1'))[2:]
        trans_count += 1
    return [trans_count, zero_count]






print(solution("110010101001"))