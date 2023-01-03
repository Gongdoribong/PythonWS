import numpy as np

# 이항관계 관계행렬 만들기
def makeRelationMatrix(A, B, R):
    datas = []
    for a in A:
        data = []
        for b in B:
            r = (a, b) 
            if r in R: data.append(1)
            else: data.append(0)
        datas.append(data)
        
    print("#관계행렬: ")
    print(np.array(datas))
    return np.array(datas)


'''
A = [1,2,3]  
R = {(1,1),(1,2),(1,3),(2,2),(3,3)}

# 이항관계 관계행렬 만들기
matrix = makeRelationMatrix(A, A, R)
'''
# 반사관계 확인: 대각성분이 모두 1인지 체크
def isReflexiveRelation(matrix):
#     print( '주대각원소: ', np.diagonal(matrix) )
    for i in np.diagonal(matrix):
        if i != 1: return False
    return True    

'''
if isReflexiveRelation(matrix): 
    print('반사관계이다')
else: 
    print('반사관계가 아니다')
'''
# 반대칭관계 확인: 주대각 원소를 기준으로 마주보는 원소가 서로 다른 값인지 체크
def isAntiSymmetricRelation(matrix):
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1: 
                return False
    return True    

'''
if isAntiSymmetricRelation(matrix): 
    print('반대칭관계이다')
else: 
    print('반대칭관계가 아니다')
'''
    # 추이관계  확인
def isTransitiveRelation(matrix):
    r2 = matrix * matrix
    r3 = matrix * matrix * matrix

    if np.array_equal(matrix, r2) and np.array_equal(matrix, r3):
        return True 
    else:
        return False

'''
if isTransitiveRelation(matrix): 
    print('추이관계이다')
else: 
    print('추이관계가 아니다')
'''
# 부분순서관계 확인
def isPartialOrderedRelation(matrix): 
    R_R = isReflexiveRelation(matrix)     # 반사관계
    A_R = isAntiSymmetricRelation(matrix) # 반대칭관계
    T_R = isTransitiveRelation(matrix)    # 추이관계
    
    if R_R and A_R and T_R:
        print('부분순서관계 이다')
        print(f'부분순서관계 여부: {True}')
        return True
    else:
        print('부분순서관계 아니다')
        print(f'부분순서관계 여부: {False}')
        return False
        
# 관계 순서쌍 만들기
def makeRelationSet(A, B):
    data = []
    for a in A:
        for b in B:
            r = (a, b)
            if (a <= b) and (b%a == 0) :
                data.append(r)
    print('#관계 순서쌍')
    print(data)
    return data

'''
A = {1,2,3,4,12}
print(f'A: {A}')

# 1-1.관계 순서쌍 만들기
R = makeRelationSet(A, A)

# 2-2.이항관계 관계행렬 만들기
matrix = makeRelationMatrix(A, A, R)

# 3.부분순서관계 확인하기
result = isPartialOrderedRelation(matrix)
'''
# 하세도형 순서쌍
def makeHasseDiagram(A, R):    
    
    # 추이관계 순서쌍 만들기
    data = []
    for r in R:        
        # 1.순회(self-loop) 제거
        if r[0] == r[1]: continue
        data.append(r)
    print('#반사관계 제거 순서쌍') 
    print(data)        
    
    skip_data = []
    for r in data:        
        for r_ in data: 
            if r[1] == r_[0] and r_[0] < r_[1]:
                t = (r[0], r_[1])
                if (t in data) and (t not in skip_data): 
                    skip_data.append(t)
    
    print('#추이관계 순서쌍') 
    print(skip_data)
    
    
    data = [] 
    for r in R:        
        # 1.순회(self-loop) 제거
        if r[0] == r[1]: continue            
        # 2.추이관계 간선 제거
        if r not in skip_data:   
            data.append(r)    
    
    print('# 하세도형 순서쌍')
    print(data)
    return data
    
'''
A = {1,2,3,4,12}
R = makeRelationSet(A, A) # 관계 순서쌍 만들기

Result = makeHasseDiagram(A, R)
'''
# 무향 그래프 그리기
def makeGraph(A, R):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()  # UndirectedGraph(무향 그래프)

    G.add_nodes_from(A) # 점 추가
    G.add_edges_from(R) # 간선 추가

    #그래프 그리기: 실행될 때마다 vertex(node)의 위치가 변경될 수 있다.)
    print('#무향그래프:')
    # 방법1: 기본 그래프
#     nx.draw(G, with_labels=True)
    # 방법2: 꾸민 그래프
    nx.draw(G, with_labels=True, 
            node_color="tab:red", node_size=800, # 노드
            edge_color="tab:blue", width=8,      # 에지
            font_size=22, alpha=0.8)

    plt.show()


A = {1,2,3,4,12}
R = makeRelationSet(A, A)       # 1.관계 순서쌍 만들기

Result = makeHasseDiagram(A, R) # 2. 하세도형 관계 만들기

makeGraph(A, Result)            # 3. 하세도형(무향 그래프) 그리기