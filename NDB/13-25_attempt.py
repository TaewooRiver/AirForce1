def countSort(list):
    res = []
    count = [0] * (max(list) + 1)
    for i in range(len(list)):
        count[list[i]] += 1
    return count

def solution(N, stages):
    answer = []
    counter = countSort(stages)
    temp = 0
    for i in range(1, len(counter)):
        clearx = counter[i]
        madeIt = 0
        for j in range(i, len(counter)):
            madeIt += counter[j]
        if madeIt <= counter[i]:
            answer.append((0, i))
        else:
            answer.append((clearx / madeIt, i))
    answer.sort(key = lambda x : (-x[0]))
    result = []
    for i in range(len(answer)):
        result.append(answer[i][1])
    
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))