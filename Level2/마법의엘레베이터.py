def solution(num):   #2554

    count = 0
    l = len(str(num))  #4

    for i in range(1,l+1):


        x = int(str(num)[-i])
        if x <= 4 or x >= 6:
            count += min(x,10-x)
            num += (x-5)//abs(x-5) * min(x,10-x) * 10**(i-1)

        elif x == 5:
            if i == l:
                count += 5
                break # continue 써도 될것같음
            y = int(str(num)[-i-1])
            if y <= 4:
                num -= 5 * 10**(i-1)
            else:
                num += 5 * 10**(i-1)
            count += 5
    return count


for i in [16, 2554]:
    print(solution(i)) # 6,16