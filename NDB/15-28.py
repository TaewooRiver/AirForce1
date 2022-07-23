def binary_search(data, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == data[mid]:
        return mid
    elif mid > data[mid]:
        return binary_search(data, mid + 1, end)
    else:
        return binary_search(data, start, mid - 1)

n = int(input())
data = list(map(int, input().split()))
res = binary_search(data, 0, n - 1)

if res == None:
    print(-1)
else:
    print(res)
    