def solution(s):
    answer = []
    # s 가 1이 될때까지 반복
    cnt = 0
    # 변환 횟수와 제거된 0의 갯수
    removed = 0
    
    while (s != "1"):
        cnt += 1
        removed += len("".join(filter(lambda x : x == '0', s)))
        # 0 제거
        c = len("".join(filter(lambda x : x == '1', s)))
        # c를 2진법으로 표현한 문자열을 s에 다시 대입
        s = str(bin(c))[2:]
        
        # print(c, s)
        # if cnt == 5:
        #     break
    
    answer.extend([cnt, removed])
        
    return answer