"""
P=[True, True, False, False]
Q=[True, False, True, False]

for i in range(4):
    print(f"P: {P[i]}\t Q: {Q[i]}\t P^Q: {P[i] and Q[i]}")

for p, q in zip(P, Q):      # 두 개를 묶어서 하나씩 빼 쓸 때 zip 사용
    print(p and q)
"""
"""
P=[True, True, False, False]
Q=[True, False, True, False]

for p, q in zip(P, Q):
    print((p and q) and (p or q))

"""
"""
P=[True, True, False, False]
Q=[True, False, True, False]

for p, q in zip(P, Q):
    print(not(p and q) and (not p or q))
"""
