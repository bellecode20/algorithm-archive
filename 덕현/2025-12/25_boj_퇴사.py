'''
boj 14501 퇴사
이거 수영장 문제같은데 DP or DFS


입력 :
N : 일 수
day : 날짜 + 가격

구조 :
dfs 날짜 넘어갈 때
날짜 상담 될때
안될때 구분해서 dfs

'''
def dfs(day_i, money_i):
    global ans

    if day_i == N:
        ans = max(ans, money_i)
        return

    if day_i > N:
        return

    if day_i + day[day_i] <= N + 1:
        dfs(day_i+day[day_i], money_i + money[day_i])

    dfs(day_i + 1, money_i)

N = int(input())
day = [0] * N
money = [0] * N


ans = 0

for i in range(N):
    a,b = map(int,input().split())
    day[i] = a
    money[i] = b

dfs(0,0)

print(ans)
