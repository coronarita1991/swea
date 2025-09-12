def solution(k, score):
    answer = []
    q = []
    for s in score :
        if len(answer) < k :
            q.append(s)
        else :
            q.sort()
            
            if s > q[0] :
                q.append(s)
                q.pop(0)
                
        # print(q)
        answer.append(min(q))
        
    return answer