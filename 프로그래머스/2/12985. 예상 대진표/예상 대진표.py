def solution(n,a,b):
    answer = 0

    if a > b :
        a, b = b, a
    
    for i in range(n):
        if 2**i >= a :
            expA = i
            break
    for i in range(expA, n):
        if 2**i >= b :
            expB = i
            break
    
    if expA == expB :
        num = 2**(expA-1) # 다음단계로
        print(num)
        return solution(n-num,a-num,b-num)
    else : 
        return expB
    
    return answer