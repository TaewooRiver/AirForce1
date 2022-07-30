n = int(input())
data = list(map(int, input().split()))
data.sort()
bulganeng = 0

if data[0] == 1:
    bulganeng = 1
else:
    bulganeng = 0
for i in range(1, len(data)):
    
    if data[i] > bulganeng + 1:
        break
    bulganeng += data[i]
print(bulganeng + 1)