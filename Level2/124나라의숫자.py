#3진법인데 3 대신 4 사용.

#print(str(0))

def solution(n):
    # i = 0
    # while True:
    #     if n // (3**i) == 0: # 3 ** (i-1) 까지 존재하는거.
    #         break
    #     i += 1
    # i -= 1   # 최고 차항.
    # # print(i)

    # mystr = ''         # 일반적인 3진법 계산
    # while i >= 0:
    #     mystr += str(n //(3**i))
    #     n = n % (3**i)
    #     i -= 1
    #  print(mystr)
    mystr = ''
    while n > 0:
        n, mod = divmod(n, 3)
        mystr += str(mod)
    mystr = mystr[::-1]    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

    while '0' in mystr:     # 문제에 맞추어 0을 3으로 바꾸어주는 과정
        k = mystr.index('0')
        # print(mystr)
        # print(k)
        l = list(mystr)
        l[k-1] = str(int(mystr[k-1]) - 1)
        l[k] = '3'
        mystr = "".join(l)
        mystr = str(int(mystr))   # 맨앞 0 없애기.

    mystr = mystr.replace('3', '4')   # 문제에 맞추어 3을 모두 4로 바꾸어주는 과정

    return mystr

print(solution(10))