import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
res = 0
while (start <= end):
    sum = 0
    
    mid = (start + end) // 2
    for x in data:
        if x > mid:
            sum += x - mid
    if sum < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
    
    

print(res)