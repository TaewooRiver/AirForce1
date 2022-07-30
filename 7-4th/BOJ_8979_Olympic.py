n, k = map(int, input().split())
nations = []
for i in range(n):
    temp = list(map(int, input().split()))
    nations.append(temp[1:])
    if temp[0] == k:
        find = temp[1:]
    
nations.sort(key = lambda x: (-x[0], -x[1], -x[2]))
print(nations.index(find) + 1)
