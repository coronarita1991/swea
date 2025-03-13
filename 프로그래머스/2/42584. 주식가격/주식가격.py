def solution(prices):
    answer = []
    
    for idx, price in enumerate(prices) :
        no_change = 0
        # 다른 가격들보다 작다면
        for j in range(idx+1, len(prices)):
            no_change += 1
            if price <= prices[j] :
                continue
            else : 
                break
        answer.append(no_change)
            
    return answer