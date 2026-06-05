def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    dp[0] = land[0]

    for i in range(1, n):
        for j in range(4):  
            temp = 0
            
            for k in range(4):
                if j == k:  continue
                temp = max(dp[i-1][k], temp)
                
            dp[i][j] = temp + land[i][j]
            
    return max(dp[-1])


def solution2(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    dp[0] = land[0]
    
    for i in range(1, n):
        for j in range(4):
            # j번째 열을 제외한 이전 행의 값들 중 최댓값 선택
            dp[i][j] = land[i][j] + max(dp[i-1][:j] + dp[i-1][j+1:])
            
    return max(dp[-1])