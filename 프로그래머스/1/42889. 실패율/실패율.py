def solution(N, stages):
    
    result = {}
    denom = len(stages)
    
    for stage in range(1, N+1):
        if denom != 0:
            count = stages.count(stage)
            # print(count)
            result[stage] = count/denom
            denom -= count
        else :
            result[stage] = 0
    
    print(result)
    return sorted(result, key = lambda x : result[x], reverse =True)