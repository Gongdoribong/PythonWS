def solution(t, p):
    t = list(map(int, t))
    p = list(map(int, p))
    tLen = len(t)
    pLen = len(p)
    loop = tLen-pLen+1
    answer = 0

    for head in range(loop):
        finish = 0
        for j in range(pLen):
            if(t[head+j] < p[j]):
                answer += 1
                finish = 1
                break
            elif(t[head+j] > p[j]):
                finish = 1
                break
        if(finish == 0):
            answer += 1

    return answer

print(solution("10203", "102"))