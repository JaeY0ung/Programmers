def solution(strings, n):
    list1 = []
    result = []
    sorted_strings = sorted(strings)   # sorted_strings
    for string in sorted_strings:
        list1.append(string[n])
        list2 = list(set(list1))
        list2 = sorted(list2)    # list2 = n th string's list
    for i in range(len(list2)):
        for string1 in sorted_strings:
            if list2[i] == string1[n]:
                result.append(string1)
    return result
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))