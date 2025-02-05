def solution(brown, yellow):
    answer = []
    
    # 카펫
    # 노랑 / 갈색 격자
    # 노랑격자 - 중앙
    # 카펫의 가로, 세로를 반환
    # 테두리의 1줄만 갈색으로 칠해져 있음!
    
    # 가로, 세로의 후보군 먼저 계산(약수)
    total = brown + yellow
    candi = [i for i in range(1, total) if total%i == 0]
    
    for h in candi: 
        for w in candi: 
            
            area = h*w
            calc_brown = 2 * (h - 1 + w - 1)
            calc_yellow = area - calc_brown
            
            if brown == calc_brown and yellow == calc_yellow :
                return [w, h]
    
#     return answer