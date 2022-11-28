from sys import stdin

def isEulerLoop(A,N) :
    check = [0]*N

    for i in range(len(A)):
        t = A[i][0]
        check[t-1]+=1

    for i in range(len(check)):
        if check[i]%2 != 0:
            return 0
    return 1

N = int(input())
mtx = [list(map(int,stdin.readline().split(" "))) for i in range(N)]
print()

M=[]
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        if mtx[i][j] == 1 :
            M.append((i+1,j+1))

#얼마전에 한 과제입니당

if isEulerLoop(M,N) == 1:
    recRes = [0]*(len(M)//2+1)  #결과 출력을 위한 리스트 생성
    recIdx = [-1]*len(M)    #한 번 갔던 길을 다시 가지 않기 위한 리스트 생성
    edge = M[0][0]  #이동할 정점 초기값
    recRes[0] = edge    #출발 정점을 결과 리스트에 담음
    for i in range(len(M)//2):
        for k in range(len(M)):
            if (k not in recIdx) and (M[k][0] == edge) :    #간 적 없는 길이고 이동한 정점과 시작점이 일치할 때
                edge = M[k][1]  #다음 정점으로 이동
                recRes[i+1] = edge  #결과 추가
                recIdx[k] = k   #중복 방지
                recIdx[M.index((M[k][1],M[k][0]))] = M.index((M[k][1], M[k][0]))    #반사관계이기 때문에 반대도 가지 않게 조치
                break
    print(' '.join(map(str,recRes)))    #결과 출력

else :
    print(-1)
