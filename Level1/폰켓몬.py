nums  = [3,1,2,3]

def solution(nums):
    getcha = len(nums) // 2   #뽑을 수 있는 폰캣몬 수
    nums1 = set(nums)
    if getcha < len(nums1):
        answer = getcha
    else:
        answer = len(nums1)
    return answer

print(solution(nums))