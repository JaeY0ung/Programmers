from copy import copy, deepcopy
from itertools import permutations as per
import re

def buho(a, b, x):
        if x == '*':
            return a * b
        elif x == '+':
            return a + b
        elif x == '-':
            return a - b

def solution(expression):
    # 초기설정
    l = len(expression)
    buho_index = []   # 부호 리스트.  ['-', '*', '-', '+']
    advance_buho_list = list(per(['*', '+', '-'], 3))
    # print(advance_buho_list)
    intarr = [int(i) for i in re.split('[*+-]', expression)] # ['100', '200', '300', '500', '20']
    answer = []
    for i in range(l):
        if expression[i] not in [str(_) for _ in range(10)]:
            buho_index.append(expression[i])
    

    for advancearr in advance_buho_list: # * + - 
        _buho_index = deepcopy(buho_index)
        _intarr = deepcopy(intarr)
        for advance in advancearr:
            i = 0
            while True:
                if advance not in _buho_index:
                        break
                if i == len(_buho_index):
                        break
                if _buho_index[i] == advance:
                    _intarr.insert(i, buho(_intarr[i], _intarr[i+1], _buho_index[i]))
                    del _intarr[i+1]
                    del _intarr[i+1]
                    del _buho_index[i]
                else: 
                    i += 1
                # print(_intarr)
        answer.append(abs(_intarr[0]))
    return max(answer)
            
        

print(solution("100-200*300-500+20"))


            
            

        
