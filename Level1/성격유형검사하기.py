def solution(survey, choices):
    R = 0
    C = 0
    J = 0
    A = 0
    for i in range(len(survey)):
        if survey[i] == "RT":
            R += 4 - choices[i]
        elif survey[i] == "TR":
            R += choices[i] - 4
        elif survey[i] == "CF":
            C += 4 - choices[i]
        elif survey[i] == "FC":
            C += choices[i] - 4
        elif survey[i] == "JM":
            J += 4 - choices[i]
        elif survey[i] == "MJ":
            J += choices[i] - 4
        elif survey[i] == "AN":
            A += 4 - choices[i]
        elif survey[i] == "NA":
            A += choices[i] - 4
    result = ''
    if R >= 0:
        result += 'R'
    else:
        result += 'T'
    if C >= 0:
        result += 'C'
    else:
        result += 'F'
    if J >= 0:
        result += 'J'
    else:
        result += 'M'
    if A >= 0:
        result += 'A'
    else:
        result = 'N'
    return result