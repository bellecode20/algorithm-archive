N, K=map(int,input().split())
objects=[list(map(int,input().split())) for _ in range(N)]  #W,V
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W,V=objects[i-1]
    for j in range(1,K+1):
        if W<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-W]+V) #넣는거랑 안넣는거 중에 더 가치가 큰거
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[N][K])