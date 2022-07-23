"""
import sys
put = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    n, m = map(int, put().split())
    data = list(map(int, input().split()))
    count = 0
    turn = m
    while data:
        temp = data[0]
        if temp == max(data):
            data.pop(0)
            count += 1
            turn -= 1
            if turn == -1:
                break
        else:
            data.pop(0)
            data.append(temp)
            turn -= 1
            if turn == -1:
                turn = len(data) - 1
        
    print(count)
"""

print("d")