
d = [0] * 100


def fibo_bottomup(x):
    d[1], d[2] = 1, 1
    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]

dd = [0] * 100

def fibo_topdown(x):
    if x == 1 or x == 2:
        return 1
    if dd[x] != 0:
        return dd[x]
    dd[x] = fibo_topdown(x - 1) + fibo_topdown(x - 2)
    return dd[x]

print(fibo_bottomup(3))
print(fibo_topdown(3))

def pibo(x):
    d[1] = 1
    d[2] = 2
    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]