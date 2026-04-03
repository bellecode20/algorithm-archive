import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))
M=int(input())
dp=[[False]*N for _ in range(N)]

for i in range(N):
    dp[i][i]=True
for i in range(N-1):
    if nums[i]==nums[i+1]:
        dp[i][i+1]=True

for length in range(3,N+1):
    for s in range(N-length+1):
        e=s+length-1
        if nums[s]==nums[e] and dp[s+1][e-1]:
            dp[s][e]=True

for _ in range(M):
    S,E=map(int,input().split())
    if dp[S-1][E-1]:print(1)
    else:print(0)