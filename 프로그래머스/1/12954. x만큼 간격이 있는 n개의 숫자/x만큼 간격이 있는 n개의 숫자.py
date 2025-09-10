def solution(x, n):
    answer = []
    if x != 0: 
        return [i for i in range(x, x*n, x)] + [x*n]
    else : 
        return [x] * n
        