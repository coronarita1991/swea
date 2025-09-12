def solution(left, right):
    answer = 0
    
    def count_div(num):
        cnt = 0
        for i in range(1, num+1):
            if num%i == 0 :
                cnt+=1
        return cnt
    
    for n in range(left, right+1):
        if count_div(n)%2 == 0 :
            answer += n
        else :
            answer -= n 
    
    return answer