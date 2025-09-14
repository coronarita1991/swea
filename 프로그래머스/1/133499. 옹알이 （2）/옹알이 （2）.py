def solution(babbling):
    SYL = ("aya", "ye", "woo", "ma")
    ans = 0

    for s in babbling:
        i = 0
        prev = ""  # 직전에 쓴 음절
        ok = True
        while i < len(s):
            matched = False
            for y in SYL:
                if s.startswith(y, i) and y != prev:
                    i += len(y)
                    prev = y
                    matched = True
                    break
            if not matched:  # 어디에도 안 맞음
                ok = False
                break
        if ok: ans += 1
    return ans