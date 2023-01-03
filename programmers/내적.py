#1. numpy 쓰기
    #TypeError: Object of type int64 is not JSON serializable => 리스트의 원소가 int가 아니여서라고 추정 (numpy)
    #아니근데 vsc는 잘 돌리잖아! 오잉 정수 배열을 받는다고 되어있는데
    #ㅇㅎ answer의 자료형이 int64여서 발생하는 오류
#2. for문 쓰기
import time
start = time.time()
'''
import numpy as np

def solution(a, b):
    answer = np.dot(a, b)
    return int(answer)
'''
'''
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
'''

a = [1,2,3,4]
b = [-3,-1,0,2]
#print(solution(a, b)) 
end = time.time()
print(f"{end - start:.10f} sec")
