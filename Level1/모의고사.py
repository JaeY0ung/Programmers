def solution(answers):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    list1 = []
    list2 = []
    list3 = []
    
    for i in range(len(answers)):
        list1.append(i % 5 + 1)
        
        if i % 2 == 0:
            list2.append(2)
        elif i % 8 == 1:
            list2.append(1)
        elif i % 8 == 3:
            list2.append(3)
        elif i % 8 == 5:
            list2.append(4)
        else:
            list2.append(5)
        
        if i % 10 == 0 or  i % 10 == 1:
            list3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            list3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            list3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            list3.append(4)
        else:
            list3.append(5)
        
        if answers[i] == list1[i]:
            sum1 += 1
        if answers[i] == list2[i]:
            sum2 += 1
        if answers[i] == list3[i]:
            sum3 += 1

    answer = []
    if sum1 == max([sum1,sum2,sum3]):
        answer.append(1)
    if sum2 == max([sum1,sum2,sum3]):
        answer.append(2)
    if sum3 == max([sum1,sum2,sum3]):
        answer.append(3)
    
    return answer

print(solution([1,2,3,4,5]))