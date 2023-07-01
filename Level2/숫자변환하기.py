def solution(x, y, n):
    
    arr_start = set()
    arr_start.add(x)
    arr_result = set()
    count = 0
    if x == y:
        return 0
    while True:
        count += 1
        for i in arr_start:
            for num in (i+n, 3*i, 2*i):
                if num < y:
                    arr_result.add(num)
                elif num == y:
                    arr_result.add(num)
                    return count
        if arr_result == set():
            return -1
        arr_start = arr_result
        arr_result = set()
