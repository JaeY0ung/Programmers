def find(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count % 2 == 0:
        return num
    else:
        return -1 * num
def solution(left, right):
    sum = 0
    for num1 in range(left, right + 1):
            sum += find(num1)
    return sum

