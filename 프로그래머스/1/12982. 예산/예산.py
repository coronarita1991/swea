def solution(d, budget):
    answer = 0
    
    for elem in sorted(d):
        if budget - elem >= 0:
            answer += 1
            budget -= elem
    
    return answer