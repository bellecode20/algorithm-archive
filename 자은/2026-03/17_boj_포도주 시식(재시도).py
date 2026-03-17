n=int(input())
wine=[ int(input()) for _ in range(n)]
dp=[[0]*3 for _ in range(n)]    #안마신거, 연속1잔, 연속2잔

dp[0][1]=wine[0]

if n>=2:    #두개 이상일때만
    for i in range(1,n):    #인덱스 두번째부터
        dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1]=dp[i-1][0]+wine[i]
        dp[i][2]=dp[i-1][1]+wine[i]

print(max(dp[n-1]))
