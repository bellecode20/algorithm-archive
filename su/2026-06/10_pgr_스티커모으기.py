'''
도둑질 문제와 동일하다.
dp[i] : i번째까지 도달했을 때 최댓값
'''

def solution(sticker):
    n = len(sticker)
    dp = [0] * n  # 첫번째 스티커를 뜯는 경우
    dp_2 = [0] * n  # 첫번째 스티커를 안 뜯는 경우
    if n <= 2:
        return max(sticker)
    
    dp[0] = sticker[0]
    dp[1] = sticker[0]  # 주의: 1번째 스티커를 뜯지 못함 -> 0번째 스티커를 뜯었을 때의 값으로 적기
    
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])  # 이전꺼 뜯는 경우 vs 지금 뜯는 경우
    
    dp_2[1] = sticker[1]
    for i in range(2, n):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + sticker[i])  # 이전꺼 뜯는 경우 vs 지금 뜯는 경우
        

    return max(dp[-2], dp_2[-1])  # 주의: dp는 첫번째 스티커를 뜯으므로 dp[-1]이 아니라 dp[-2]여야 함