n, k = map(int, input().split())
medal = []
for i in range(n):
    medal.append(list(map(int, input().split())) + [1])

medal.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if medal[i-1][1:4] == medal[i][1:4]:
        medal[i][4] = medal[i-1][-1]
    else:
        medal[i][4] = i + 1
    
    if k == medal[i][0]:
        print(medal[i][-1])
        break
