import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

com_len = int(input())
move = []
for i in range(com_len):
    move.append(input().strip().split())


cur_dir = 1
cur_com = 0

snake = deque()
snake.append([0,0])
board[0][0] = 2

while True:
    cur = snake[0]
    n_x, n_y = cur[0] + dx[cur_dir], cur[1] + dy[cur_dir]

    if n_x < 0 or n_y < 0 or n_x >= n or n_y >= n or board[n_x][n_y] == 2:
        result += 1
        break
    
    if board[n_x][n_y] == 1:
        snake.appendleft([n_x, n_y])
        board[n_x][n_y] = 2
    else:
        prev = snake.pop()
        board[prev[0]][prev[1]] = 0
        snake.appendleft([n_x, n_y])
        board[n_x][n_y] = 2
    result += 1

    if cur_com < com_len:
        if result == int(move[cur_com][0]):
            if move[cur_com][1] == "L":
                cur_dir -= 1
                if cur_dir < 0:
                    cur_dir =3
            else:
                cur_dir += 1
                if cur_dir > 3:
                    cur_dir = 0
            cur_com += 1
print(result)