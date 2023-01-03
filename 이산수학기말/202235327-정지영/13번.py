import numpy as np

# 인접행렬 만들기
def makeAdjacencyMatirx(V, E, W):

    # 빈(0) 행렬 만들기
    adj = [[0 for _ in range(len(V))] for _ in range(len(V))]
    i = 0
    # 인접 행렬 만들기
    for t in E:
        src, dest = t
        adj[src-1][dest-1] = W[i]
        i+=1

    print(np.array(adj) )        
    return np.array(adj) 

# 연결리스트 만들기
def makeLinkedList(V, E):
    
    adj = [[] for _ in range(len(V))]

    for t in E:
        src, dest = t    
        adj[src-1].append(dest)
    

    for idx, v in enumerate(adj):
        v.sort()
        print(f'v[{idx+1}]의 연결 리스트 =  {v}')
        
    return adj




V = [1,2,3,4,5,6]
E = [(1,2),(1,4),(1,6),(2,3),(2,6),(3,4),(4,2),(5,4),(5,6),(6,4)]
W = [3,4,5,1,1,2,3,3,2,2]

print('#유향 그래프 인접행렬:')
makeAdjacencyMatirx(V, E, W)
print()
print('#유향 그래프 연결리스트:')
makeLinkedList(V, E)  # 유향 그래프 인접리스트