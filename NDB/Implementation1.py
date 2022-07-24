n = int(input())
data = [[0]*n for _ in range(n)]
plan = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x = 1
y = 1

for i in plan:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
        
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x = nx
        y = ny

pritn(x, y)