def find(parent, i):
    # i 가 속한 집합의 루트 찾기
    if parent[i] == i:
        return i
    
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    # root찾기
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        # 연결
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        # 연결
        parent[yroot] = xroot
        
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    answer = 0
    # cost : u, v, weight
    # 비용이 저렴한 것 부터 정렬
    costs.sort(key=lambda x:x[2])
    
    # 각 노드의 부모 추적하는 배열
    parent = [i for i in range(n)]
    # 각 노드의 트리 랭크를 추적 하는 배열
    rank = [0] * n
    
    # 총 비용
    min_cost = 0 
    edges = 0 # 간선의 개수
    
    for edge in costs:
        if edges == n-1 : 
            # n-1개의 간선만이 있다면 중단 (최소신장트리 속성)
            break
        
        # 현재 간선의 두 노드가 속한 집합의 루트 찾기
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x!=y : # 서로 다른 집합에 속하는 경우 합치기
            union(parent, rank, x, y)
            
            # 현재 간선의 비용을 최소 비용에 추가
            min_cost += edge[2]
            
            edges+=1
    
    return min_cost
    
    return answer