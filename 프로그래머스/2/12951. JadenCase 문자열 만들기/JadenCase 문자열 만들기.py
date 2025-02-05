def solution(s):

    # 첫 단어 대문자로
    # 공백문자가 연속해서 나올 수 있음.
    
    
    words = s.split(" ")
    res = []
    
    
    for w in words :
        if len(w) == 0 : # 연속 된 공백을 이렇게 추가 가능함. 
            res.append(w)
        else :
            first_char = w[0].upper()
            rest = w[1:].lower()
            
            new_word = first_char + rest
            res.append(new_word)
    
    return " ".join(res)