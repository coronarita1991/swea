def solution(n):
    answer = 0
    
    # '연속'된 '자연수'로 표현하는 법 - 구간합?
    arr = [i for i in range(1, n+1)]
    
    for i in range(n):
        for j in range(i+1, n):
            if sum(arr[i:j]) == n :
                answer += 1
            elif sum(arr[i:j]) > n :
                break
            else :
                continue
    
    return answer+1