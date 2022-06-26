n = int(input())
data = list(map(int, input().split()))
data.sort()
people = 0
parties = 0
for x in data:
    people += 1
    if x <= people:
        parties += 1
        people = 0
    
print(parties)
