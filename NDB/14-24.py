n = int(input())
data = list(map(int, input().split()))
data.sort()
# 데이터를 정렬한 후 이를 이용해 중간값(median) 도출
print(data[(n - 1) // 2])

