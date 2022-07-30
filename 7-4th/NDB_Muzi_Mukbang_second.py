import heapq
def solution(food_times, k):
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))
    food_num = len(food_times)
    previous = 0
    while h:
        t = (h[0][0] - previous) * food_num
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break
    return answer



#print(solution([3, 1, 2], 5))
#print(solution([8, 6, 4], 15)) # 2