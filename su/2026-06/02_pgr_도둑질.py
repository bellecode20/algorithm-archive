def solution(money):
    n = len(money)
    dp = [0] * n   # dp 첫번째 집 터는 경우
    dp_safe = [0] * n  # dp 첫번째 집 안 터는 경우
    
    dp[0] = money[0]
    dp[1] = money[0]  
    
    for i in range(2, n-1):  # 첫 집을 턴 경우
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    
    dp_safe[1] = money[1]  # 첫번째 집 안터는 경우
    for i in range(2, n):  # 첫 집을 안 턴 경우
        dp_safe[i] = max(dp_safe[i-1], dp_safe[i-2] + money[i])
    
    
    return max(dp_safe[-1], dp[-2])
    