import copy

def solution(expression):   #  "100-200*300-500+20"
    arr_oper = []
    for oper in expression:
        if oper not in [str(i) for i in range(10)]:
            arr_oper.append(oper)
    # print(arr_oper)      ['-', '*', '-', '+']
    exp = expression.replace('*','+').replace('-','+')
    arr_int = exp.split('+')
    # print(arr_int)       ['100', '200', '300', '500', '20']
    list1 = [['*','+','-'], ['*','-','+'], ['+','*','-'], ['+','-','*'], ['-','+','*'], ['-','*','+']]
    maxInt = 0

    for list2 in list1:
        arr_oper1 = copy.deepcopy(arr_oper)
        arr_int1 = copy.deepcopy(arr_int)
        for oper in list2:     # '-' in ['*','+','-']
            for k in arr_oper1: # '-' in ['-', '*', '-', '+']
                if k == oper:
                    i = arr_oper1.index(k)
                    if oper == "*":
                        k = int(arr_int1[i]) * int(arr_int1[i+1])
                    elif oper == "+":
                        k = int(arr_int1[i]) + int(arr_int1[i+1])
                    else:
                        k = int(arr_int1[i]) - int(arr_int1[i+1])
                
                    del arr_int1[i]
                    arr_int1[i] = str(k)
                    del arr_oper1[i]

        #     if arr_oper1 != []:
        #         if arr_oper1[0] == "*":
        #             k = int(arr_int1[0]) * int(arr_int1[1])
        #         elif arr_oper1[0] == "+":
        #             k = int(arr_int1[0]) + int(arr_int1[1])
        #         else:
        #             k = int(arr_int1[0]) - int(arr_int1[1])
        #     maxInt = abs(k)
        # print(arr_int1, arr_oper1)


        maxInt = max(abs(int(arr_int1[0])), maxInt)
    return maxInt


print(solution("100-200*300-500+20"))    #	answer: 60420