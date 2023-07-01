def solution(n):
    x = n + 1
    y = bin(n).count('1')
    while True:
        if bin(x).count('1') == y:
            return x
        x += 1