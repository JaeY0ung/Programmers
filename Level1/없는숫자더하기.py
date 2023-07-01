def solution(nums):
    list = []
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums) -1):
            for k in range(j+1, len(nums)):
                s = nums[i] + nums[j] + nums[k]
                list.append(s)
    # print(list)
    for l in list:
        for p in range(2,l):
            if l % p == 0:
                break
            if p == l-1:
                answer += 1
    return answer

nums = [1,2,3,4]
print(solution(nums))