def solution(numbers):            # 다시풀어 성공!!!!
    myarr1 = [str(num) for num in numbers]
    l = 4
    myarr2 = []
    # for num in myarr1:   # l : max 문자열의 길이
    #     if len(num) > l:
    #         l = len(num)
    for num in myarr1:
        x = num * (l // len(num))
        x += x[:l % len(num)]
        myarr2.append((num, int(x)))
    # print(myarr2)
    myarr3 = sorted(myarr2, key=lambda x : -x[1])
    # print(myarr3)
    answer = ''
    for num in myarr3:
        answer += num[0]
    return str(int(answer))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))