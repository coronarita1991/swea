def solution(s):
    
    st = []
    # baabaa - b 'aa' baa - 'bb' aa - 'aa'
    
    for ch in s: 
        if len(st) == 0 : 
            st.append(ch)
        else : 
            if ch == st[-1] : 
                st.pop()
            else : 
                st.append(ch)
        # print(st)
    
    return 1 if len(st) == 0 else 0