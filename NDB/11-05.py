n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
sum = 0
for x in data:
    for i in range(len(data)):
        if x < data[i]:
            sum += 1

print(sum)

