def solution(ingredient):
    ingLen = len(ingredient)
    stack = list()
    answer = 0
    #0 아무것도 아닌거
    #1 빵
    #2 빵 야채
    #3 빵 야채 고기
    #4 빵 야채 고기 빵
    
    if ingredient[0] == 1:
        stack.append(1)
    else:
        stack.append(0)
    
    for i in range(1, ingLen):
        last = 0
        if len(stack) > 0:
            last = stack.pop()
        if ingredient[i]>=2 and last == ingredient[i]-1:    #빵 이후 순서가 순서에 맞으면
            stack.append(last+1)    #스택에 다음 재료 넣기
        elif ingredient[i] == 1 and last == 3:  #덮는 빵이면
            answer += 1 #햄버거 완성
        elif ingredient[i] == 1:    #빵이면
            stack.append(last)  #스택에 last 넣고 빵을 넣는다...?
            stack.append(1)
        else:   #다 해당 안되면
            stack.append(last)  #스택에 last 넣고 0을 넣는다...
            stack.append(0)
    return answer