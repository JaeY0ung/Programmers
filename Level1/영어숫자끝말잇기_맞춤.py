# print(5%2)  # 나머지
# print(5//2) # 몫
# words = [1,3,3,3,4]
# print(words[0:3])
def solution(n, words):
    num1 = 100
    num2 = 100
    num3 = 100
    for i in range(len(words)):
        if len(words[i]) == 1:
            num1 = i           # num 이 틀린사람 리스트 번째.
            break
    for j in range(len(words)-1):
        if words[j][-1] != words[j+1][0]: #시작단어 끝단어 
            num2 = j + 1
            break
    for k in range(len(words)):
        if words[k] in words[0:k]:   #중복 안됌
            num3 = k
            break
    num = min(num1,num2,num3)
    if num == 100:
        return [0,0]
    else:
        answer =  [num % n + 1, num // n + 1]
    
    return answer

words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(3,words))