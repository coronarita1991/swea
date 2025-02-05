def solution(n):
    ans = 0
    
    return len(list(filter(lambda x : x == "1", str(bin(n))[2:])))