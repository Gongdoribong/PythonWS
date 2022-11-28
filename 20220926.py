"""
N = set(range(10))
evens = { 2 * n for n in N }
powers = { 2 ** n for n in N }
print(N)
print(evens)
print(sorted(powers))
"""

N={n for n in range(1,11)}
print(sorted(N))