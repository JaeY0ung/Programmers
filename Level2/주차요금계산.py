from math import ceil
def solution(fees, records):
    dic = dict()
    while True:
        x = records[0][6:10]  # 차량번호
        for i in range(1, len(records)): 
            if records[i][6:10] == x:
                # print(records[0], records[i])
                time = ( int(records[i][:2]) - int(records[0][:2]) ) * 60 + int(records[i][3:5]) - int(records[0][3:5])
                if x in dic.keys():
                    time = time + dic[x]
                    dic.update({x : time})
                else:
                    dic.update({x : time})
                del records[i]
                del records[0]
                break
            if i == len(records) - 1 :   # 출차 내역 없을때.
                time = ( 23 - int(records[0][:2]) ) * 60 + 59 - int(records[0][3:5])
                if x in dic.keys():
                    time = time + dic[x]
                    dic.update({x : time})
                else:
                    dic.update({x : time})
                del records[0]
                break
        if len(records) == 0:
            break
    dic = sorted(dic.items())
    #print(dic)
    result = []
    for arr in dic:
        if arr[1] <= fees[0]:
            pay = fees[1]
        else:
            pay = fees[1] + ceil( (arr[1] - fees[0])/fees[2] ) * fees[3]
        result.append(pay)
    return result
        

print(solution([180, 5000, 10, 600], \
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", \
        "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))