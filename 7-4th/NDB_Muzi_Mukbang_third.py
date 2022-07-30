import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    h = []
    sum_value = 0
    length = len(food_times)
    prev = 0
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))
    
    while sum_value + (h[0][0] - prev) * length <= k:
        now = heapq.heappop(h)[0]
        sum_value += (now - prev) * length
        length -= 1
        prev = now

    result = sorted(h, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]
print(solution([3, 1, 2], 5))