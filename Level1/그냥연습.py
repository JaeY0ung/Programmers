# map(함수, 리스트 or 튜플의 변수명)
a = [1.5 , 1.9 , 13.5]
b = list(map(int, a))
print(b)

a = [3,4,5,2,4,3,5,13,91]

def mul(n):
    n *=3
    return n
    
print(list(map(mul,a)))


x = "i am student, you are a girl"
b= x.split()  # 괄호안에 어떤 문자를 기준으로 분리할지 적습니다.
print(b)

a,b,c = map(int,input().split())
print(a)
print(b)
print(c)