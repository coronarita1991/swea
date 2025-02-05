from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    
    progresses = [(k, v) for k, v in zip(progresses, speeds)]
    
    n = 0
    
    while not all(map(lambda x: x[0]>=100, progresses)):
        q.clear()
        for idx, (cur_progress, speed) in enumerate(progresses):
            
            # 공정률 업데이트
            if cur_progress < 100 : 
                q.append((cur_progress + speed, speed))
            
            else : 
                # 현상유지
                q.append((cur_progress, speed))
        
        cnt = 0
        print(q)
        while len(q) and q[0][0] >= 100 : 
            q.popleft()
            cnt += 1
        
        if cnt :
            answer.append(cnt)
        
        # if n == 20:
        #     break
        n+=1
        progresses = list(q)[::]
        
    return answer