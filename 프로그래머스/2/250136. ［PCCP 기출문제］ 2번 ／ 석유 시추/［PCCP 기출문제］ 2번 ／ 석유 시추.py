from collections import deque, defaultdict

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    BFS_MAP = [[0 for _ in range(m)] for _ in range(n)]
    count_info = defaultdict(int)
    
    def bfs(x, y, area_num):
        q = deque()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        cnt = 1
        q.append((x, y))
        BFS_MAP[x][y] = area_num
        
        def in_range(x, y):
            return 0<=x<n and 0<=y<m
        
        while q:
            x, y = q.popleft()
            
            # print(x, y, cnt)    
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny) : continue
                if BFS_MAP[nx][ny] : continue
                if not land[nx][ny]: continue
                q.append((nx, ny))
                BFS_MAP[nx][ny] = area_num
                cnt += 1
        
        count_info[area_num] = cnt
        
        # return cnt
    
    # 열 방향 순회
    # for col in range(m):
    #     answer = max(answer, calc_oil(col))
        
    # 최적화 
    # 1. BFS MAP을 구하기 (쪼개진 영역 - 1, 2, 3, 4 / 각 영역 별 카운트 수 딕셔너리 매핑)
    area_num = 1
    for row in range(n):
        for col in range(m):
            if not BFS_MAP[row][col] and land[row][col] : 
                bfs(row, col, area_num)
                area_num += 1
    
#     for _ in range(n):
#         print(*BFS_MAP[_])
    
    # 2. BFS MAP으로 col방향 순회 하면서, 해당 좌표에 영역 있으면, set으로 더하기
    for col in range(m):
        area_check = set()
        for row in range(n):
            if land[row][col]:
                area_check.add(BFS_MAP[row][col])
        # print(area_check)
        # 3. 총 답은 set에 있는 키-val의 합계        
        tot = sum([count_info[i] for i in list(area_check)])
        # print(tot)
        answer = max(answer, tot)
    
    return answer