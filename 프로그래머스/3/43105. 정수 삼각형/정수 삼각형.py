def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    
    # 초기값 설정
    dp[0][0] = triangle[0][0]
    
    # DP 점화식 적용
    for i in range(1, n):
        for j in range(i + 1):  # i번째 행은 j가 0 ~ i까지 존재
            if j == 0:
                # 왼쪽 가장자리의 경우, 위에서 내려오는 경우만 존재
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == i:
                # 오른쪽 가장자리의 경우, 왼쪽 대각선에서만 내려옴
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                # 일반적인 경우, 두 가지 경로 중 최댓값 선택
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    # 마지막 행에서 최댓값 반환
    return max(dp[-1])