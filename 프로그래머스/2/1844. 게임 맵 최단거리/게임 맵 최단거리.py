from collections import deque

def solution(maps):
    answer = 0
    
    n, m = len(maps), len(maps[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs():
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        # dist 계산 진행
        q = deque()
        dist[0][0] = 1
        visited[0][0] = 1
        q.append((0, 0))
        
        def in_range(x, y):
            return 0<=x<n and 0<=y<m
        
        while q : 
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if not in_range(nx, ny) or visited[nx][ny] : continue
                if not maps[nx][ny] : continue
                
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
        
    bfs()
    
    
    
    if dist[n-1][m-1] == -1:
        return -1
    else : 
        answer = dist[n-1][m-1]
        
    return answer