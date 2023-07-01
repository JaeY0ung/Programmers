def solution(n):
    if n==1 or n==2 or n==4:
        return 1
    elif n==3 or n==5 or n ==6:
        return 2
    else: #n>=7
        count = 0
        for i in range((n+2)//4):
            if n % (2*i+1) == 0:
                if n//(2*i+1) - i >= 1:
                    count += 1
            if n % (2*i+2) == i+1:
                if n//(2*i+2) - i >= 1:
                    count += 1
        return count
    