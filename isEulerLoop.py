def matrix(n, choice):  #입력 받기
    mtx = []
    if choice == 1 : stg = "행"
    else : stg = "원소"

    for i in range(n):
        m = input(f"{i+1}번째 {stg} 입력 (띄어쓰기로 구분)").split(" ")
        mtx.append(list(map(int,m)))

    return(mtx)

def makeElm(A) :  #인접행렬을 요소로 전환
    M=[]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 1 :
                M.append((i+1,j+1))
    return(M)

def isEulerLoop(A) :    #오일러 루프인지 확인
    A.sort()
    rowMax = A[len(A)-1][0]
    check = [0]*rowMax
    
    for i in range(len(A)): #각 정점의 차수 카운팅
        t = A[i][0]
        check[t-1]+=1
        if rowMax < A[i][1]:
            return 0
    
    for i in range(len(check)): #각 정점의 차수가 짝수인지 확인
        if check[i]%2 != 0:
            return 0
    return 1


menu = int(input("""\
오일러 루프 판별 프로그램입니다.
1 : 인접행렬로 입력하기
2 : 원소로 입력하기
숫자를 입력해주세요 : """))

if menu == 1 :  #인접행렬일 경우
    a_size = int(input("행렬의 행 길이를 입력하세요 :"))
    adjMax = matrix(a_size, 1)
    A = makeElm(adjMax)
    
elif menu == 2: #원소일 경우
    a_num = int(input("원소의 개수를 입력하세요 : "))
    A = matrix(a_num, 2)

else:
    print("잘못 입력하셨습니다.")


if isEulerLoop(A) == 1 :    #결과 출력
    print("오일러 루프가 맞습니다.")
elif isEulerLoop(A) == 0 :
    print("오일러 루프가 아닙니다.")