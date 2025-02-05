
def solution(A,B):
    answer = 0
    # A, B에서 하나씩 쌍을 지어야 함.    
    '''
    누적합이 작아지려면, 큰값과 작은 값을 곱해야 함. 
    '''    
    
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += a*b    
    
    return answer