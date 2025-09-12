def solution(s, n):
    answer = ''
    # 시저 암호
    # 각 알파벳은 n만큼 밀고, 대소문자는 따로
    for ch in s : 
        if ch == ' ':
            answer += ch
            
        else : 
            # Z -> A가 되게 해야됨
            if ch.islower():
                answer+=chr((ord(ch)-ord('a')+n)%26+ord('a'))
            else :
                answer+=chr((ord(ch)-ord('A')+n)%26+ord('A'))
    
    return answer