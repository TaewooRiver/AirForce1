def solution(s):
    
    sum = 0
    for x in s:
        if x == "p" or x == "P":
            sum += 1
        elif x == "y" or x == "Y":
            sum -= 1
        
    if sum == 0:
        return True
    else:
        return False

print(solution("pPoooyY"))