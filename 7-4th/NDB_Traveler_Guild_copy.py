n = int(input())
count = 0
fears = list(map(int, input().split()))
thresh = 0
for fear in fears:
    thresh += 1
    if thresh >= fear:
        thresh = 0
        count += 1

print(count)