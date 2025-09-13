def solution(name, yearning, photo):
    # from collections import defaultdict
    score_dict = {k:v for k, v in zip(name, yearning)}
    answer = []
    
    def calculate_score(p):
        score = 0
        for elem in p : 
            if score_dict.get(elem):
                score += score_dict[elem]
        
        return score
    
    for p in photo : 
        answer.append(calculate_score(p))
    return answer