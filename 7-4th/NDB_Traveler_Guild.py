n = int(input())
count = 0
fears = list(map(int, input().split()))
fears.sort()
thresh = 1
for fear in fears:
    if thresh >= fear:
        count += 1
        thresh = 1
    else: 
        thresh += 1

print(count)