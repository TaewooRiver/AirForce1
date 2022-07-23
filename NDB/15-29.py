import sys
input = sys.stdin.readline
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
    
data.sort()
res = 0
start = 1
end = data[-1] - data[0]

while (start <= end):
    mid = (start + end) // 2
    count = 1
    value = data[0]
    for i in range(1, n):
        if data[i] >= value + mid: # (방금 전 공유기 설치한 집의 좌표 + 거리의 임시 하한선)보다 i번째 집이 더 클 경우 == 
            value = data[i] # 공유기 설치
            count += 1 # 공유기 개수 증가 <- 만약 이게 c보다 커지면, 거리의 임시 하한선을 mid보다 큰 범위에서 탐색한다(이진탐색)
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)
