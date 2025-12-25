n = int(input())
t_lst = []
p_lst = []

for _ in range(n):
    t, p = map(int, input().split())
    t_lst.append(t)
    p_lst.append(p)

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + t_lst[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p_lst[i] + dp[i + t_lst[i]])

print(dp[0])