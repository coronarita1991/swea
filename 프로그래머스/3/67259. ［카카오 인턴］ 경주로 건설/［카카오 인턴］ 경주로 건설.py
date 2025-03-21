def is_valid(x, y, N):
    # 보드 범위 확인
    return 0<=x< N and 0<=y<N

def is_blocked(x, y, board, N):
    # 주어진 좌표가 차단 / 이동 불가 확인
    return (x, y) == (0, 0) or not is_valid(x, y, N) or board[x][y] ==1 

def calculate_cost(direction, prev_direction, cost):
    # 이전 방향/ 현재방향의 일치여부 따라 계산
    if prev_direction == -1 or (prev_direction - direction)%2 ==0:
        return cost + 100
    else:
        return cost + 600
    
def is_should_update(x, y, direction, new_cost, visited):
    # 주어진 좌표와 방향이 방문 하지 않았거나 새 비용이 더 작은 경우
    return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost
    
def solution(board):
    N = len(board)
    # 방향 : 상, 좌, 하, 우
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    queue = [(0, 0, -1, 0)]     # (x, y, prev_dir, cost)
    answer = float("inf")
    
    # 큐 빌 때까지 반복
    while queue:
        x, y, prev_direction, cost = queue.pop(0)
        
        # 모든 방향 탐색
        for direction, (dx, dy) in enumerate(directions):
            new_x, new_y = x+dx, y+dy
            # 이동 할 수 없는 좌표 건너뛰기
            if is_blocked(new_x, new_y, board, N):
                continue
            
            new_cost = calculate_cost(direction, prev_direction, cost)
            
            # 도착지 도달 시 최소비용 갱신
            if (new_x, new_y) == (N-1, N-1):
                answer = min(answer, new_cost)
            
            # 좌표와 방향이 아직 미방문 /새 비용이 더 작은 경우 큐에 추가
            elif is_should_update(new_x, new_y, direction, new_cost, visited):
                queue.append((new_x, new_y, direction, new_cost))
                visited[new_x][new_y][direction] = new_cost
    
    return answer