import heapq
def solution(food_times, k):
    length = len(food_times)
    h = []
    for i in range(length):
        heapq.heappush(h, (food_times[i], i + 1))
    
    food_num = len(food_times)
    prev = 0

    while h:
        now, _ = heapq.heappop(h)
        deletetime = (now - prev) * k
        if k > deletetime:
            k -= deletetime
            prev += now
            food_num -= 1
        elif k == deletetime:
            return 1
        else:
            foods = h.sort(key = lambda x: x[1])
            left_time = now - prev
            while left_time > food_num:
                left_time -= food_num 
            for i in range(1, food_num + 1):
                left_time -= 1
                if left_time == 0:
                    return i + 1


print(solution([3, 1, 2], 5))
print(solution([8, 6, 4], 15)) # 2