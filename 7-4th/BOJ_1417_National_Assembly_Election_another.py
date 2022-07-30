n = int(input())
n_vote = []
for i in range(n):
    n_vote.append(int(input()))

cand = n_vote[1:]
dasom = n_vote[0]
count = 0

if n == 1:
    print(0)
else:
    cand.sort(reverse=True)
    while dasom <= cand[0]:
        cand[0] -= 1
        dasom += 1
        count += 1
        cand.sort(reverse=True)
    print(count)