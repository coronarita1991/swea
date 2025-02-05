

def solution(n):
    answer = 0
    
    # 조건 - n의 '다음 큰 숫자'
    # 크면서, 2진수 변환 시 1의 수 같고
    # 가장 작은 수
    
    def num_of_1(n):
        return len(list(filter(lambda x: x == '1', str(bin(n))[2:])))
    
    cnt1 = num_of_1(n)
    candi = n + 1
    
    while True :     
        cnt2 = num_of_1(candi)
        if cnt1 == cnt2 : 
            break
            
        candi += 1
        
    return candi