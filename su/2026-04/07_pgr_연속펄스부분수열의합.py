def solution(sequence):
    answer = 0
    N = len(sequence)
    dp = [[0] * 2 for _ in range(N+1)]  # 누적합. dp[i][0]: i번째 수(1곱한경우)까지의 최대합, dp[i][1]: i번째수(-1곱한 경우)까지의 최대합
    reversed_seq = [-x for x in sequence]
    
    
    for i in range(N):
        if i == 0:
            dp[0][0] = sequence[0]
            dp[0][1] = reversed_seq[0]
            answer = max(max(dp[0]), answer)
            continue
            
        dp[i][0] = max(sequence[i], dp[i-1][1] + sequence[i])  # 부분수열 새로 시작하기 vs 기존 부분수열에 i번째 수 더하기
        dp[i][1] = max(reversed_seq[i], dp[i-1][0] + reversed_seq[i])
        answer = max(max(dp[i]), answer)
            
    return answer