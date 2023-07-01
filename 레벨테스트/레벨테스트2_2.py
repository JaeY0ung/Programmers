from math import ceil
def solution(progresses, speeds):
    arr1 = [ ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    print(arr1)
    for i in range(len(arr1)-1):
        if arr1[i] > arr1[i+1]:
            arr1[i+1] = arr1[i]
    dic = list(dict.fromkeys(arr1))
    answer = []
    for i in dic:
        answer.append(arr1.count(i))
    return answer

print(solution(	[93, 30, 55], [1, 30, 5]))
