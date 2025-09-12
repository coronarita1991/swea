def solution(food):
    answer = ''
    food_key = {i:k for i,k in enumerate(food)}
    
    for k, v in food_key.items():
        if k == 0 : 
            # answer += str(v)
            continue
        else :
            n = v//2
            answer = answer + str(k)*n
            # answer = str(k)*n + answer
    
    answer = answer + '0' + answer[::-1]
    
    return answer   