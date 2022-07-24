import sys
put = sys.stdin.readline

n, k = map(int, input().split())
country = list()
find = []
for i in range(n):
    temp = list(map(int, input().split()))
    country.append(temp[1:])
    if temp[0] == k:
        find = temp[1:]
country.sort(key=lambda x: (-x[0], -x[1], -x[2])

print(int(country.index(find) + 1)
