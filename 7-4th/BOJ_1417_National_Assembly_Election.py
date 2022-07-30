n = int(input())
candids = []
for i in range(n):
    temp = int(input())
    candids.append([i + 1, temp])
    if i == 0:
        my_votes = temp
count = 0
candids.sort(key= lambda x: -x[1])
my_rank = candids.index([1, my_votes])
more_than_me = 0
for i in range(n):
        if candids[i][1] >= candids[my_rank][1]:
            more_than_me += 1
while more_than_me != 1:
    if n == 1:
        break
    more_than_me = 0

    if my_rank != 0:
        candids[0][1] -= 1
    else:
        candids[1][1] -= 1
    candids[my_rank][1] += 1
    my_votes += 1
    count += 1
    candids.sort(key= lambda x: -x[1])
    my_rank = candids.index([1, my_votes])

    for i in range(n):
        if candids[i][1] >= candids[my_rank][1]:
            more_than_me += 1




print(count)