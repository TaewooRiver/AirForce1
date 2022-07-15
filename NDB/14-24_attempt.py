
def swapListElement(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

def countSort(list):
    count = [0] * (max(list) + 1)
    res = []
    for i in range(len(list)):
        count[list[i]] += 1
    for i in range(len(count)):
        res.append(count[i])
    return count

def checkDist(list, spot):
    res = 0
    
    for house in list:
        res += abs(spot - house)
    return res


n = int(input())
data = list(map(int, input().split()))

maxd = max(data)
mind = min(data)
result = 987654321
val = 0
for i in range(mind, maxd + 1):
    temp = checkDist(data, i)
    
    if result > temp:
        result = temp
        val = i
print(val)