def solution(n):
    answer = 0
    
    if n == 1:
        return (n+1)**2
    
    # 제곱근 판별
    for i in range(1, n//2+1):
        if i*i == n :
            return (i+1)**2
    
    return -1