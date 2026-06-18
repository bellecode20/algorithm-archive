def solution(a):
    INF = int(1e9)
    answer = 0
    n = len(a)
    min_memo = [[INF, INF] for _ in range(n)]
    
    min_memo[0][0] = a[0]
    for i in range(1, n): 
        min_memo[i][0] = min(min_memo[i-1][0], a[i])
    
    min_memo[n-1][1] = a[-1]
    for i in range(n-2, -1, -1):
        min_memo[i][1] = min(min_memo[i+1][1], a[i])
        
    
    for i in range(n):
        left_min = min_memo[i][0]
        right_min = min_memo[i][1]
        cur = a[i]
        if cur > left_min and cur > right_min:  # 양 끝값도 어차피 자기 자신이기 때문에 이 조건 만족할 수 없어서 answer 카운팅 됨
            continue
        answer += 1
        
    return answer