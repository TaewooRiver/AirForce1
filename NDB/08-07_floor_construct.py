n = int(input())
data = [0] * 1000
data[0] = 1
data[1] = 3
for i in range(2, n):
    data[i] = (data[i - 1] + data[i - 2] * 2) % 796796

print(data[n - 1])