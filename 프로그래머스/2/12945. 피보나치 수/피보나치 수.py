def solution(n):
    answer = 0
    
    # memoization / dp
    fibo_list = [0] * (n+1)
    fibo_list[1] = 1
    
    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    
    return fibo_list[n] % 1234567