import math

def solution(arr):
    answer = 1
    # 최소공배수 두수 씩 확장하기
    for n in arr:
        answer = (answer*n) // math.gcd(n, answer)
    return answer
    