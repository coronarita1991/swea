def solution(s):
    answer = ''
    # 소문자가 먼저 오고, 알파벳 역순으로
    s = sorted(s, reverse=True)
    return ''.join(s)