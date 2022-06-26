data = input()
sum = 0
for i in range(len(data)):
    num = int(data[i])
    if sum != 0 and num != 0:
        sum *= num
    else:
        sum += num

print(sum)

