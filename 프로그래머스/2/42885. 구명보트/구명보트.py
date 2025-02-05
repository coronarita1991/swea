def solution(people, limit):
    
    
    '''그리디
    
    최대한 적게 구명보트 사용하여 구출 - 최대 2명씩 / 무게제한 limit 
    
    '''
    people.sort()
    answer = 0
    
    l, r = 0, len(people) -1
    
    while l<= r: 
        if people[l] + people[r] <= limit :
            l += 1
        
        r -= 1
        answer += 1
        
    
    return answer