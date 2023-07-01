# def solution(phone_book):     # 1
#     x = sorted(phone_book, key = len)
#     l = len(x)
#     result = True
#     for i in range(l-1):
#         for j in range(i+1,l):
#             if x[i] == x[j][:len(x[i])]:
#                 result = False
#                 break
#         if result == False:
#             break
#     return result

# def solution(phone_book):    # 2
#     l = len(phone_book)
#     result = True
#     for i in range(l):
#         for j in range(l):
#             if i == j:
#                 continue
#             elif len(phone_book[i]) >= len(phone_book[j]):
#                 continue
#             elif phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 result = False
#                 break
#         if result == False:
#             break
#     return result


# def solution(phone_book):    # 3
#     l = len(phone_book)
#     result = True
#     for i in range(l):
#         for j in range(l):
#             if i == j:
#                 continue
#             if len(phone_book[i]) < len(phone_book[j]):
#                 if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                     result = False
#                     break
#             elif len(phone_book[i]) > len(phone_book[j]):
#                 if phone_book[j] == phone_book[i][:len(phone_book[j])]:
#                     result = False
#                     break
#         if result == False:
#             break
#     return result

def solution(phone_book):    # 4  드디어 통과!! sort 의 기본을 생각하자.
    x = sorted(phone_book)
    result = True
    for i in range(len(x)-1):
        if x[i] == x[i+1][:len(x[i])]:
            result = False
            break
    return result


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123","456","789"])) # True