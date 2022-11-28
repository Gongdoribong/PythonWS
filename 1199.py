from sys import stdin

def isEulerLoop(A,N) :
    check = [0]*N
    odd = 0
    last = 0

    for i in range(len(A)):
        t = A[i][0]
        if t != last :
            last = t
        check[t-1]+=1

    for i in range(len(check)):
        if check[i]%2 != 0:
            odd += 1

    if odd == 2 or odd == 0:
        return(1)
    else:
        return(0)

N = int(input())
mtx = [list(map(int,stdin.readline().split(" "))) for i in range(N)]

M = [(i+1,j+1) for i in range(len(mtx)) for j in range(len(mtx[0])) for k in range(mtx[i][j]) if mtx[i][j] != 0]

if isEulerLoop(M,N) == 1:
    recRes = [0]*(len(M)//2+1)
    recIdx = [-1]*len(M)
    edge = M[0][0]
    recRes[0] = edge
    for i in range(len(M)//2):
        for k in range(len(M)):
            if (k not in recIdx) and (M[k][0] == edge) :
                edge = M[k][1]
                recRes[i+1] = edge
                recIdx[k] = k
                recIdx[M.index((M[k][1],M[k][0]))] = M.index((M[k][1], M[k][0]))
                break
    print(' '.join(map(str,recRes)))

else :
    print(-1)
