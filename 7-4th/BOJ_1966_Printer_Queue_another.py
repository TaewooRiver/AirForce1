cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    
    order = 0
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'
    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))

