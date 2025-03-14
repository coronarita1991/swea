from itertools import combinations # 안 쓰고 어떻게 하지 ?
from collections import defaultdict

def solution(orders, course):
    # 손님 번호 order
    count_dict = defaultdict(int)
    for course_num in course : 
        for order in orders:
            cases = list(combinations(order, course_num))
            for case in cases:
                
                count_dict[''.join(sorted(list(case)))] += 1
    
    # print(count_dict)
                
    answer = []
    
    # 각 개수 별 최댓값 주워담기
    for course_num in course:
        max_val = 0
        temp = []
        for case, val in count_dict.items():
            if len(case) == course_num and val >= 2: 
                temp.append([case, val])
                if val > max_val:
                    max_val = val
        
        for comp in temp : 
            if comp[1] == max_val:
                answer.append(comp[0])
            # print(temp)
        
    return sorted(answer)