data = [7,5,9,0,3,1,6,2,4,8]

def swapListElement(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

count = [0] * (max(data) + 1)

for i in range(len(data)):
    count[data[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')