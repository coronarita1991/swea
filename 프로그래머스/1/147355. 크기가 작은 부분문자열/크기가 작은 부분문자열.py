def solution(t, p):
    answer = 0
    
    # 같은 길이인지 ?
    l = len(p)
    
    # 부분문자열 순회
    for i in range(len(t) - l+1):
        target = int(t[i:i+l])
        
        if target <= int(p):
            # print(target)
            answer+=1
    
    return answer