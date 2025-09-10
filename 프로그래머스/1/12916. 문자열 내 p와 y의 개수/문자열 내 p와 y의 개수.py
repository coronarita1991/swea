def solution(s):
    answer = True
    cnt_p = cnt_y = 0
    s = s.lower()

    for ch in s:
        if ch == 'p':
            cnt_p += 1
        elif ch == 'y' :
            cnt_y += 1
    print(cnt_p, cnt_y)
    return cnt_p == cnt_y