

def solution(participant, completion):
    for name in completion:
        if name in participant:
            participant.remove(name)
    answer = participant[0]
    return answer

def solution(participant, completion):
    completion.sort()
    participant.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    return answer