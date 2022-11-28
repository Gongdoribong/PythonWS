import random

A=[]
n=[]
breaker = False

while len(A)<20:
    x = random.randint(-100, 100)
    if x not in A :
        A.append(x)

print(A)

for i in A:
    print("i값:",i)
    for j in A[A.index(i)+1:]:
        print("j값:",j)
        if -(i+j) in A[A.index(j)+1:]:
            n.append(0)
            breaker = True
            break
    if breaker == True:
        break

if 0 in n:
    print(0)
else:
    print(-1)