def solution(a, b):
    answer = 0
    
    for _a, _b in zip(a, b):
        answer += _a*_b
    
    return answer