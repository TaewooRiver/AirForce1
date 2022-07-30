import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())
t = 0
field = []
bombs_first = []
bombs_second = []
dirs = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]
for i in range(R):
    temp = input()
    field.append([char for char in temp])
    for j in range(C):
         if temp[j] == 'O':
            bombs_first.append([i, j])

true_time = N%4

while t <= true_time + 4:
    if N == 1 or N == 0 or true_time == 0 or true_time == 2:
        break
    if t == 1 or t == 0:
        t += 1
        continue
    if t % 4 == 2:
        for i in range(R):
            for j in range(C):
                if field[i][j] == '.':
                    bombs_second.append([i, j])
                    field[i][j] = 'O'
        field_2 = field
    elif t % 4 == 0:
        for i in range(R):
            for j in range(C):
                if field[i][j] == '.':
                    bombs_first.append([i, j])
                    field[i][j] = 'O'
        field_0 = field
    elif t % 4 == 1:
        while bombs_second:
            bomb = bombs_second.pop(0)
        
            for i in range(4):
                n_bomb_r, n_bomb_c = bomb[0] + dirs[i][0], bomb[1] + dirs[i][1]
                if 0 <= n_bomb_r < R and 0 <= n_bomb_c < C:
                    field[n_bomb_r][n_bomb_c] = '.'
                    if [n_bomb_r, n_bomb_c] in bombs_first:
                        bombs_first.remove([n_bomb_r, n_bomb_c])
                                            
            field[bomb[0]][bomb[1]] = '.'
        field_1 = field


    else:
        while bombs_first:
            bomb = bombs_first.pop(0)
        
            for i in range(4):
                n_bomb_r, n_bomb_c = bomb[0] + dirs[i][0], bomb[1] + dirs[i][1]
                if 0 <= n_bomb_r < R and 0 <= n_bomb_c < C:
                    field[n_bomb_r][n_bomb_c] = '.'
                    if [n_bomb_r, n_bomb_c] in bombs_second:
                        bombs_second.remove([n_bomb_r, n_bomb_c])
            field[bomb[0]][bomb[1]] = '.'
        field_3 = field
    t += 1

if N == 1 or N == 0:
    for row in field_0:
        print(''.join(row))
else:
    real_t = N%4
    full_field = ['O'*C for _ in range(R)]
    if real_t == 0 or real_t == 2:
        for row in full_field:
            print(''.join(row))
    elif real_t == 1:
        for row in field_1:
            print(''.join(row))
    else:
        for row in field_3:
            print(''.join(row))


