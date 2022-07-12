import sys
f = sys.stdin.readline
n, m = map(int, f().split())
data = []
temp = [[0]*m for _ in range(n)]
res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    data.append(list(map(int, f().split())))
def vir(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny < m and ny >= 0:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                vir(nx, ny)
def get_score():
    scr = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                scr += 1
    return scr

def dfs(count):
    global res
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    vir(i, j)
        res = max(res, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(res)