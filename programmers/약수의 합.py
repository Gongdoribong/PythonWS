n = 12
t = 0
answer = 0

while(t!=n):
    t+=1
    if(n%t==0):
        answer+=t

print(answer)