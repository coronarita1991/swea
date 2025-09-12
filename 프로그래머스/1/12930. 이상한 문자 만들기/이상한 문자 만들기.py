def solution(s):
    answer = ''
    temp = []
    def transform_word(word):
        nw = ''
        for i, ch in enumerate(word):
            if i % 2 == 0:
                nw += ch.upper()
            else : 
                nw += ch.lower()
        return nw
             
    # 단어 추출
    words = s.split()
    for word in words:
        temp.append(transform_word(word))

    import re
    
    # 임시로 _ 치환
    s = s.replace(' ', '_')
    s = re.sub(r'[A-Za-z]+', '^', s)
    
    for ch in s :
        if ch == '^': 
            answer+=temp.pop(0)
        else:   
            answer += ' '
    
    
    
    
    return answer