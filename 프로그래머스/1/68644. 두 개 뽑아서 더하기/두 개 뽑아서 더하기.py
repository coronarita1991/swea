# permutations import
from itertools import permutations

def solution(numbers):
    
    
    sum = []
    temp = list(permutations(numbers, 2))
    for i in temp : 
        sum.append(i[0] + i[1])
    
    answer = sorted(set(sum))
    return answer