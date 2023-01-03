

def solution(ingredient):
    making = 1
    answer = 0

    for i in range(len(ingredient)):
        if(answer != i):
            break
        for j in range(len(ingredient)):
            if(ingredient[j] == making):    #다음에 와야 하는 재료이면
                making += 1
            elif(ingredient[j] == 1 and making == 4):   #마지막 빵
                making = 1
                answer += 1
                del ingredient[j-3:j+1]
                break
            else:   #재료 틀리면 리셋
                if(ingredient[j]==1):
                    making = 2
                else:
                    making = 1

    return answer