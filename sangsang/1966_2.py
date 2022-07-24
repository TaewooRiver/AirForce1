
import sys
input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    count = 0
    target = m
    while q:
        temp = q[0]
        if temp == max(q):
            q.pop(0)
            target -= 1
            count += 1
            if target < 0:
                break
            
        else:
            q.pop(0)
            q.append(temp)
            target -= 1
            if target < 0:
                target = len(q) - 1

    print(count)