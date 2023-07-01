def solution(a,b,n):   # 611위
    count = 0
    cola = n
    while cola >= a:
        temp = cola
        cola %= a
        cola += (temp // a) * b
        count += (temp // a) * b
    return count
