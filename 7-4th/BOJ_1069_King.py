
# A -> column
# 1 -> row

# R -> (0, 1)
# L -> (0. -1)
# B -> (-1, 0)
# T -> (1, 0)
# RT -> (1, 1)
# LT -> (1, -1)
# RB -> (-1, 1)
# LB -> (-1, -1)

#stone_row
#stone_col
#king_row
#king_col

directions = [
    [0,1],
    [0,-1],
    [-1,0],
    [1,0],
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1]
]

names = ['R','L','B','T','RT','LT','RB','LB']


king, stone, com_len = input().strip().split()
move = []
for i in range(int(com_len)):
    move.append(input().strip())
king = [int(king[1]), ord(king[0])-64]
stone = [int(stone[1]), ord(stone[0])-64]


for i in move:
    for j in range(8):
        if i == names[j]:
            n_king_r, n_king_c = king[0] + directions[j][0], king[1] + directions[j][1]
            if n_king_r < 1 or n_king_r > 8 or n_king_c < 1 or n_king_c > 8:
                continue
            if n_king_r == stone[0] and n_king_c == stone[1]:
                stone_r, stone_c = stone[0] + directions[j][0], stone[1] + directions[j][1]
                if stone_r < 1 or stone_r > 8 or stone_c < 1 or stone_c > 8:
                    continue
                stone[0], stone[1] = stone_r, stone_c

            
            king[0], king[1] = n_king_r, n_king_c
            

print(chr(king[1] + 64) + (str(king[0])))
print(chr(stone[1] + 64) + (str(stone[0])))

