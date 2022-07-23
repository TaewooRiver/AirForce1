import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
queries = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for x in queries:
    if binary_search(data, x, 0, n - 1) == None:
        print(0)
    else:
        print(1)