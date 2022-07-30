cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    turn = m
    count = 0
    while que:
        temp = que[0]
        if temp == max(que):
            que.pop(0)
            count += 1
            turn -= 1
            if turn == -1:
                break
        else:
            que.pop(0)
            que.append(temp)
            turn -= 1
            if turn == -1:
                turn = len(que) - 1
    print(count)
