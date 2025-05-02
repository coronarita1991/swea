import datetime

def solution(lines):
    combined_log = []
    # 파싱
    import time
    
    for line in lines:
        log = line.split()
        timestamp = datetime.datetime.strptime(log[0] + ' ' + log[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        
        combined_log.append((timestamp, -1)) # 완료시점
        combined_log.append((timestamp - float(log[2][:-1]) + 0.001, 1)) # 시작시점
    
    
    # print(combined_log)
    
    # 순회 - 슬라이딩 윈도우
    accumulated = 0
    max_requests = 1
    
    combined_log.sort(key=lambda x: x[0])
    
    for i, elem1 in enumerate(combined_log):
        current = accumulated
        
        # 1초 미만 윈도우 범위 내 계산
        for j, elem2 in enumerate(combined_log[i:]):
            
            if elem2[0] - elem1[0] >= 1 : 
                break
                
            if elem2[1] == 1 :
                current += elem2[1]
                
        max_requests = max(max_requests, current)
        accumulated += elem1[1]
        
    return max_requests