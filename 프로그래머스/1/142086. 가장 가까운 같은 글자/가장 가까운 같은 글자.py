def solution(s):
    answer = []
    
    # banana
    # b, a, n : 처음나와서 -1, 각각 idx 저장(0, 1, 2)
    # a (3) -> 1의 위치 : 3-1 반환 및 3 갱신
    # n (4) -> 2의 위치 : 4-2 반환 및 4 갱신
    
    pos = dict()
    
    for idx, ch in enumerate(s):
        if pos.get(ch) is None : # 아직 없다면
            answer.append(-1)
        else : # 있다면
            answer.append(idx - pos[ch])
        pos[ch] = idx
            
    
    return answer