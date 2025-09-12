def solution(s):
    answer = ''
    
    # 일부 자릿수를 영단어로 변경
    # 영어를 숫자로
    
    # key : digit, number
    num_map = {'zer':(4, 0),'one':(3, 1),'two': (3, 2),
    'thr': (5, 3),'fou': (4, 4),'fiv': (4, 5),'six': (3, 6),
    'sev': (5, 7),'eig': (5, 8),'nin': (4, 9),}
    
    cur = 0
    while cur != len(s):
        # 조사
        if s[cur].isdigit():
            answer += s[cur]
            cur+=1
        else :
            cur_key = s[cur:cur+3]
            digit, num = num_map[cur_key]
            cur += digit
            answer += str(num)
    
    
    return int(answer)