def solution(numbers):
    arr = []
    for number in numbers:
        result = True
        x = bin(number)[2:]
        x = x[::-1]   #거꾸로.
        x = list(x)
        for i in range(len(x)):
            if x[i] == '0':
                x[i]  = '1'
                if i != 0:
                    x[i-1] = '0'
                break
            result = False
        if result == False:
            x[-1] = '0'
            x.append('1')
        print(x)
        k = ''.join(x[::-1])
        arr.append(int(k,2))
    return arr

print(solution([2,7]))

