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

left_chicken = list(combinations(chicken, m))

min_city = 1e9
for i in left_chicken:
    city_model = 0
    for j in house:
        min_house = 1e9
        for k in i:
            min_house = min(min_house, abs(j[0]-k[0]) + abs(j[1]-k[1]))
        city_model += min_house
    min_city = min(min_city, city_model)

print(min_city)
