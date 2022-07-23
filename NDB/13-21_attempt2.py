import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def process(x, y, index):
    nationsUnited = []
    nationsUnited.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[x][y] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    nationsUnited.append((nx, ny))
    for i, j in nationsUnited:
        graph[i][j] = summary // count

total_count = 0

while True:
    index = 0
    union = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1
    