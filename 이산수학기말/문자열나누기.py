words=[]
result=[]

cnt_x = 0
cnt_notx = 0

s = input()
s = list(s)
x = s[0]

for i in range(len(s)):
    words.append(s[i])
    if s[i] == x:
        cnt_x += 1

    else:
        cnt_notx += 1

    if cnt_x == cnt_notx or i == len(s)-1:
        result.append(''.join(words))
        words=[]    
        cnt_x = 0
        cnt_notx = 0
        if i != len(s)-1:
            x = s[i+1]



print(len(result))
