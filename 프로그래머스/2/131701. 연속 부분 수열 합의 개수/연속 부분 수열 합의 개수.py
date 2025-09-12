def solution(elements):
    answer = 0
    a = set()
    l = len(elements)
    
    # 원순열
    elements = elements + elements
    
    # slice길이
    for i in range(1,l+1):
        # 시작 Idx
        for j in range(l):
            
            a.add(sum(elements[j:j+i]))
    # print(a)
    
    return len(a)