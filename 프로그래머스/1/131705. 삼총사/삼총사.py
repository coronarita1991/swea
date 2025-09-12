def solution(number):
    answer = 0
    
    # 삼총사 - 합이 0..?
    from itertools import combinations
    
    for case in combinations(number, 3):
        if sum(case) == 0:
            answer+=1
    
    return answer