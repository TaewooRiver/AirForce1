# n by n 도시
# 치킨 거리는 abs(r1 - r2) + abs(c1 - c2)
# 0 빈칸 1 집 2 치킨집
# 치킨 거리들 중에서 최솟값이 한 집의 치킨 거리
# m개의 치킨집만 남긴다고 했을 때
# 도시의 치킨거리가 최소화되는 경우
from itertools import combinations
n, m = map(int, input().split())
city = []
house = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            house.append([i, j])
        elif temp[j] == 2:
            chicken.append([i, j])
    city.append(temp)

left_chicken = list(combinations(chicken, m))

min_city = 1e9
one_city = 0
for i in left_chicken:
    one_city = 0
    for j in house:
        min_house = 1e9
        for k in i:
            min_house = min(min_house, abs(j[0] - k[0]) + abs(j[1] - k[1]))
        one_city += min_house
    min_city = min(min_city, one_city)

print(min_city)
