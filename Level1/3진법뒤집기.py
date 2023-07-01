def solution(n):         #45
    i = -1
    while True:
        if n // (3**i) != 0:
            i += 1
        else:
            break        # i = 4
    j = i -1             # j = 3

    str_3 = ''
    while j >= 0:
        str_3 += str(n // (3**j))
        n -= ( n // (3**j) ) * (3**j)
        j -= 1                     # str_3 = 1200
    reversed_str_3 = str_3[::-1]   # reversed_str_3 = 0021

    int_10 = 0
    for k in range(i):
        int_10 += int(reversed_str_3[-k-1]) * (3**k)
    return int_10


print(solution(45))