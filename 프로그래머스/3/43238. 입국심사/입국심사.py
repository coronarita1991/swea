def solution(n, times):
    answer = 0
    
    # right 가장 비효율적인 시간 :
    # 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사 받는 경우
    l, r = 1, max(times) * n 
    
    while l <= r :
        mid = (l + r) // 2
        people = 0
        
        for time in times:
            # people : 모든 심사관들이 mid 분 동안 심사 한 수
            people += mid // time
            # 모든 심사관 거치지 않아도, n명 이상 심사 가능
            if people >= n:
                break
        
        # 심사 한 사람의 수가 심사 받아야할 사람의 수보다 많거나 같다면
        if people >= n:
            answer = mid
            r = mid - 1
        else :
            l = mid + 1
    
    return answer