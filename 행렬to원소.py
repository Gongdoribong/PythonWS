A=[[0,1,1],[1,0,1],[1,1,0]]
M=[]
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == 1 :
            M.append((i+1,j+1))

print(M)