from collections import deque
n = int(input())
k = int(input())
board = [[0]*n for i in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1
com_len = int(input())
commands = []
for _ in range(com_len):
    commands.append(input().strip().split())


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
snake = deque()
snake.append([0,0])
orient = 1
cur_com =0

t = 0

while True:
    cur = snake[0]
    n_x, n_y = cur[0] + directions[orient][0], cur[1] + directions[orient][1]
    if n_x < 0 or n_y < 0 or n_x >= n or n_x >= n or board[n_x][n_y] == 2:
        t += 1
        break
    
    if board[n_x][n_y] == 1:
        snake.appendleft([n_x, n_y])
        board[n_x][n_y] = 2
    else:
        prev = snake.pop()
        board[prev[0]][prev[1]] = 0
        snake.appendleft([n_x,n_y])
        board[n_x][n_y] = 2
    
    t += 1

    if cur_com < com_len:
        if t == int(commands[cur_com][0]):
            if commands[cur_com][1] == 'L':
                orient -= 1
                if orient == -1:
                    orient = 3
            else:
                orient += 1
                if orient == 4:
                    orient = 0
            cur_com += 1

print(t)




