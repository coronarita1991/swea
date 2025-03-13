def solution(n, left, right):
    answer = []

    # left-1, right-1 까지 순회하면서, 
    
    for idx in range(left, right+1):
        # 행(i) - left // n 
        # 열(j) - right % n
        # 2차원 좌표 구하고
        i = idx // n 
        j = idx % n 
        # 해당 좌표를 통해 
        val = j+1 if j > i else i+1
        
        answer.append(val)
                    
    

    return answer            
            
    