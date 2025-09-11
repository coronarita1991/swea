def solution(s):
    # 길이 확인
    l = len(s)
    if l == 4 or l == 6 : 
        return not any(ch for ch in s if ch.isalpha())
    return False