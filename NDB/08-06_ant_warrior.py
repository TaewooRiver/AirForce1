n = int(input())
data = list(map(int, input().split()))
teoll_ja = [0]*(n+1)
teoll_ja[0] = data[0]
teoll_ja[1] = max(data[0], data[1])
for i in range(2, n):
    teoll_ja[i] = max(teoll_ja[i-2] + data[i], teoll_ja[i-1])

print(teoll_ja[n - 1])