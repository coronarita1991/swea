def solution(n):
    answer = 0
    return int(''.join(sorted(str(n), reverse=True)))