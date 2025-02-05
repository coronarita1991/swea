def solution(n):
    answer = 0
    
    if n == 1 :
        return 1
    
    
    num_list = [0] * (n+1)
    num_list[1] = 1
    num_list[2] = 2
    
    for i in range(3, n+1):
        num_list[i] = num_list[i-2] + num_list[i-1]
    
    return num_list[n] % 1234567