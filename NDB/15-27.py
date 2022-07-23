def process(array, x):
    n = len(array)
    a = starter(array, x, 0, n - 1)
    if a == None:
        return 0
    b = stopper(array, x, 0, n - 1)

    return b - a + 1


def starter(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return starter(array, target, start, mid - 1)
    else:
        return starter(array, target, mid + 1, end)

def stopper(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return stopper(array, target, start, mid - 1)
    else:
        return stopper(array, target, mid + 1, end)

n, x = map(int, input().split())
data = list(map(int, input().split()))

count = process(data, x)
if count == 0:
    print(-1)
else:
    print(count)