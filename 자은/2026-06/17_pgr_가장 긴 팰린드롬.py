def solution(s):

    n=len(s)
    dp=[[False]*n for _ in range(n)]
    
    for i in range(n):dp[i][i]=True
    
    for i in range(n-1):    #길이 2일때
        if s[i]==s[i+1]:
            dp[i][i+1]=True
    
    for l in range(3,n+1):    #길이 3이상 검사
        for i in range(n-l+1):
            j=i+l-1 #마지막 인덱스
            if s[i] != s[j]:continue    #시작과 마지막이 다르면 패스
            if dp[i+1][j-1]:
                dp[i][j]=True
    
    for l in range(n,0,-1):
        for i in range(n-l+1):
            if dp[i][i+l-1]:
                return l
    return 1