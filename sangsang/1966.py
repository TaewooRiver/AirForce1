import sys
put = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n, m = map(int, put().split())
    data = list(map(int, put().split()))
    count = 0
    position = m
    while data:
        temp = data[0]
        if temp == max(data):
            data.pop(0)
            position -= 1
            count += 1
            if position == -1:
                break
        else:
            data.pop(0)
            data.append(temp)
            position -= 1
            if position == -1:
                position = len(data) - 1
    print(count)