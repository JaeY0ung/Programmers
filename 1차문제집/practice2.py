def solution(want, number, discount):
    days = 0
    for i in range(len(discount) - 9):    # i + 9 가 len(discount) -1 일때까지.
        count = 0
        listNumber = []
        list1 = discount[i: i + 10]
        for things in want:
            listNumber.append(list1.count(things))
        if listNumber == number:
            days += 1
    return days
        



print(solution(["banana", "apple", "rice", "pork",  "pot"], \
    [3,2,2,2,1], ["chicken", "apple", "apple", "banana", "rice", "apple", \
        "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
