def solution(s):
    
    res = []
    tmp = ''
    if s[0] == s[1]:
        res = ['']
    else:

        tmp += str(s[0])
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] or s[i] == s[i + 1]:
            if tmp != '':
                res.append(tmp)
            tmp = ''
        else:
            tmp += str(s[i])
    if s[-1] == s[-2]:
        if tmp != '':
            res.append(tmp)
        res.append("")
    else:
        tmp += str(s[-1])
        res.append(tmp)

    return res

print(solution("pizza"))
print(solution("mississippi"))
print(solution("aabcddddefggg"))
print(solution("abyyy"))
print(solution("kkkkkkk"))  