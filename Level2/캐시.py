def solution(casheSize, cities):
    l = len(cities)
    my_arr = []
    time = 0
    if casheSize == 0:
        return 5*l
    for city in cities:
        city = city.lower()
        if city in my_arr:
            my_arr.remove(city)
            my_arr.append(city)
            time += 1
        else:   # 안들어있다면
            if len(my_arr) == casheSize:  # 캐시 꽉 찼다면.
                del my_arr[0]
            my_arr.append(city)
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))