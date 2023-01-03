def recursion(n):
    if n<=18 :
        return n + recursion(n+1)
    else:
        return 2+1


n = 1
print(f'n={n}, recursion(n) = {recursion(n)}')
