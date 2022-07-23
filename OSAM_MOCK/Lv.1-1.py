def compareAnswer(list, answer, n):
    count = 0
    for i in range(n):
        if list[i] == answer[i]:
            count += 1
    return count


def solution(answers):
    answer = []
    fail_1 = []
    fail_2 = []
    fail_3 = []
    length = len(answers)
    while length > 0:
        temp = 1
        while temp <= 5:
            fail_1.append(temp)
            length -= 1
            temp += 1
        
    length = len(answers)
    for i in range(length):
        temp = 1
        if (i%8) == 0 or (i%8) == 2 or (i%8) == 4 or (i%8) == 6 or i == 0:
            fail_2.append(2)
        elif (i%8) == 1:
            fail_2.append(1)
        elif (i%8) == 3:
            fail_2.append(3)
        elif (i%8) == 5:
            fail_2.append(4)
        else:
            fail_2.append(5)


    for i in range(length):
        if i == 0 or (i % 10) == 0 or (i % 10) == 1:
            fail_3.append(3)
        elif (i % 10) == 2 or (i % 10) == 3:
            fail_3.append(1)
        elif (i % 10) == 4 or (i % 10) == 5:
            fail_3.append(2)
        elif (i % 10) == 6 or (i % 10) == 7:
            fail_3.append(4)
        else:
            fail_3.append(5)
    
    correct_1 = compareAnswer(fail_1, answers, len(answers))
    correct_2 = compareAnswer(fail_2, answers, len(answers))
    correct_3 = compareAnswer(fail_3, answers, len(answers))
    res = [correct_1, correct_2, correct_3]
    
    maximum = max(res)
    if res[0] == maximum:
        answer.append(1)
    if res[1] == maximum:
        answer.append(2)
    if res[2] == maximum:
        answer.append(3)

    

    return answer

#print(solution([1,3,2,4,2]))