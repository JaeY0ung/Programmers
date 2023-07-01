from itertools import combinations as co

def solution(numbers, target):
    l = len(numbers)
    answer = 0
    if sum(numbers) == target: # - 가 0개.
        answer += 1
    for i in range(1, l+1):  # - 가 1 ~ l 개.
        for arr in list(co(range(l),i)):
            numsum = 0
            # print(arr)
            for k in range(l):
                if k in arr:
                    numsum -= numbers[k]
                else:
                    numsum += numbers[k]
            if numsum == target:
                answer += 1
    return answer

print(solution([4, 1, 2, 1], 4))
    