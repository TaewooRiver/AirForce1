n = input()
res = 0
for i in range(len(n)):
    if res == 0 or res == 1 or int(n[i]) == 0 or int(n[i]) == 1:
        res += int(n[i])
    else:
        res *= int(n[i])
    
print(res)