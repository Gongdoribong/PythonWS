# 정수 판별 프로그램
'''def is_integer(N):
    if N - int(N) == 0 :
        print(f'{N}은 정수이다')
    if N - int(N) != 0 :
        print("소수")

try:
    N = float(input('숫자를 입력하세요: '))
    #N = float(N)
    is_integer(N)

#숫자가 아닌 것을 입력받았을 때
except ValueError:
    print("math error")

#자료형 확인 함수 : type()
#print(type())
'''
'''
#소수 판별하기
import math
def is_prime_number(x):
    for i in range(2,x+1):
        if x % i == 0 and x != i :
            return False
    return True

# 자연수 N 입력
x = int(input("\n소수 판별하기 위한 정수 값을 입력해 주세요: "))

if is_prime_number(x):
    print(' Prime number!\n')
else:
    print(' Not Prime number!\n')
'''

'''
#암스트롱수
a=[]
for n in range(100,1000):
    h=n//100
    t=n//10-h*10
    o=n%10
    if h**3+t**3+o**3 == n :
        a.append(n)
print(a)
'''
'''
import numpy as np  #as는 이름 설정

arr1 = np.array([[5,2],[10,3]])
arr2 = np.array([3000,5000])

result = np.linalg.solve(arr1,arr2)
print(result)
print(result.dtype)
'''