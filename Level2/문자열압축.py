def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1): #i개씩 나눌거임. 
        mylist = []
        a = 0
        for _ in range( len(s) // i ):
            mylist.append(s[a : a+i])
            a += i
        if len(s) % i != 0:
            mylist.append(s[a:])
        # print(mylist)
        a = 0
        b = 0
        mylist2 = [] 
        sum = ""
        for j in range(len(mylist) - 1):
            if mylist[j] != mylist[j+1]:
                a = b
                b = j+1
                mylist2.append(mylist[a:b])
            if j == len(mylist) - 2:
                mylist2.append(mylist[b:])
        for _ in mylist2:
            if len(_) == 1:
                sum += _[0]
            else:
                sum += str(len(_)) + _[0]
        answer.append(len(sum))
        # print(sum)
    return min(answer)

                
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))