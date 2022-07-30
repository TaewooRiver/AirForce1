n = input().strip()
length = len(n) // 2
chk = True
a = 0
b = 0
for i in range(length):
    a += int(n[i])
    b += int(n[-(i+1)])


if a == b:
    print("LUCKY")
else:
    print("READY")