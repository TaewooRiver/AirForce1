n = input()
temp = True
count = 0
for i in range(len(n)):
    if n[0] != n[i] and temp == True:
        count += 1
        temp = False
    if n[0] == n[i] and temp == False:
        count += 1
        temp = True

print(count // 2)