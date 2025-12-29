def dfs(idx, player):
    global mn

    if player == n // 2:
        team1, team2 = [], []
        for i in range(n):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)
        
        team1_sum = 0
        team2_sum = 0
        
        for i in range(len(team1)):
            for j in range(i+1, len(team1)):
                team1_sum += data[team1[i]][team1[j]] + data[team1[j]][team1[i]]

        for i in range(len(team2)):
            for j in range(i+1, len(team2)):
                team2_sum += data[team2[i]][team2[j]] + data[team2[j]][team2[i]]
        
        mn = min(mn, abs(team1_sum - team2_sum))
        return

    for i in range(idx, n):
        visited[i] = 1
        dfs(i + 1, player + 1)
        visited[i] = 0


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
mn = float('inf')

dfs(0, 0)
print(mn)