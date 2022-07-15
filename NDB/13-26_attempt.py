n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

def addRecursive(list, start, end):
    if end == 1:
        return 0
    sum = 0
    for i in range(start, end):
        sum += list[i]
    return (sum + addRecursive(list, start, end - 1))

print(addRecursive(data, 0, n))
