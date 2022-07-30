from collections import deque
nums = deque()
k = int(input())
for i in range(k):
    temp = int(input())
    if temp == 0:
        nums.pop()
    else:
        nums.append(temp)
print(sum(nums))
