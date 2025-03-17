def solution(maps):
    from collections import deque
    answer = 0
    N = len(maps)
    M = len(maps[0])
    # 초기화
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E' :
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    
    def in_range(x, y):
        return 0<=x<N and 0<=y<M
    
    # L까지 먼저 BFS
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 0
    
    def bfs(target):
        # print(visited, q)
        while q :
            x, y = q.popleft()
            
            if (x, y) == (target[0], target[1]):
                break
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                # print(nx, ny)
                if not in_range(nx, ny): continue
                if maps[nx][ny] == 'X': continue
                if visited[nx][ny]<0: 
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                
    bfs([lx, ly])
    
    if visited[lx][ly]<0 :
        return -1
    # print(visited)
    cnt = visited[lx][ly]
    # 초기화
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([lx, ly])
    visited[lx][ly] = 0

    # E까지 BFS 최종
    bfs([ex, ey])
    
    # print(visited)
    if visited[ex][ey]<0 :
        return -1
    
    
    return cnt + visited[ex][ey]