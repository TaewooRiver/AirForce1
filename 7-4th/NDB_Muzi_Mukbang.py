import heapq
def solution(food_times, k):
    h = []
    if sum(food_times) <= k:
        return -1
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    previous = 0
    length = len(food_times)
    while ((h[0][0] - previous) * length) <= k:
        now = heapq.heappop(h)[0]
        k -= (now - previous) * length
        previous = now
        length -= 1
    
    result2 = sorted(h, key = lambda x: x[1])
    return result2[k % length][1]

#print(solution([3, 1, 2], 5))
#print(solution([8, 6, 4], 15)) # 2