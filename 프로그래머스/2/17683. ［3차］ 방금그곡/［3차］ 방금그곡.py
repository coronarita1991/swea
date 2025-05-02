import re

def solution(m, musicinfos):
    answer = []
    pattern = r'[A-Z]#?'
    
    m_note = re.findall(pattern, m)
    
    def calc_time(t1, t2):
        h1, m1 = map(int, t1.split(':'))
        h2, m2 = map(int, t2.split(':'))
        return (h2-h1)*60 + (m2-m1)
    
    
    for musicinfo in musicinfos : 
        s, e, title, notes = musicinfo.split(',')
        duration = calc_time(s, e)

        note = re.findall(pattern, notes)
        
        if duration >= len(note) : 
            record = [] 
            for _ in range(duration):
                record.append(note[_%len(note)])
            
        else : 
            record = note[:duration]
        
        
        # 확인
        for i in range(len(record) - len(m_note) + 1):
            # print(''.join(record[i:i+len(m_note)]))
            if m == ''.join(record[i:i+len(m_note)]):
                answer.append((duration, title))
                break
    
    # print(answer)
    
    answer.sort(key=lambda x: -x[0])
    if not answer :
        return '(None)'
    
    return answer[0][-1]