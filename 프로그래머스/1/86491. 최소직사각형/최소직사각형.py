def solution(sizes):
    answer = 0
    w, h = [], []
    for size in sizes:
        a, b = size
        # a가 더 크다고 가정
        if a < b : 
            a, b = b, a
            
        w.append(a)
        h.append(b)
        
    # print(w, h)
    
    
    return max(w) * max(h)