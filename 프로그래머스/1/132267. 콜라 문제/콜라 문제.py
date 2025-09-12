def solution(a, b, n):
    answer = 0
    # 병 교환 진행
    while n >= a :
        # a병 가져다주면 b병 준다.
        answer += (n//a) * b # 받은 병
        mod = n%a # 남은 병
        tmp = (n//a) * b # 
        n = tmp + mod
        # print(answer)
    return answer