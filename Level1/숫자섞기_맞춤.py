def solution(numbers):
    
    list1 = [numbers[0]+numbers[1]]
    length = len(numbers)
    for i in range(length - 1):
        for j in range(i+1, length):
            sum = numbers[i] + numbers[j]
            list1.append(sum)
    list1.sort()
    list1 = set(list1)
    list1 = list(list1)
    # for _ in range
    # for i in range(len(list)-1):
    #     if list[i] == list[j]:
    return list1

# numbers = [0,1,2,3,4]
# print(solution(numbers))
# answer = []
# return answer
# if sum > list[-1]:
#     list.append(sum)
# elif sum < list[-1]: